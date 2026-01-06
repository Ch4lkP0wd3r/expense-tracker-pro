"""
Personal Expense Tracker - Professional Edition
A robust command-line application for tracking and analyzing personal expenses.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
from datetime import datetime
from typing import Optional, Dict, List
from pathlib import Path
import json


class ExpenseTracker:
    """Main class for managing personal expenses with data validation and persistence."""
    
    # Configuration constants
    DATA_DIR = Path('data')
    REPORTS_DIR = Path('reports')
    BACKUP_DIR = Path('backups')
    DATA_FILE = DATA_DIR / 'expenses.csv'
    REPORT_FILE = REPORTS_DIR / 'summary_report.csv'
    CONFIG_FILE = DATA_DIR / 'config.json'
    
    # Predefined categories for consistency
    CATEGORIES = [
        'Food & Dining',
        'Transportation',
        'Entertainment',
        'Shopping',
        'Bills & Utilities',
        'Healthcare',
        'Education',
        'Groceries',
        'Other'
    ]
    
    def __init__(self):
        """Initialize the expense tracker and load existing data."""
        self._setup_directories()
        self.df = self._load_data()
        self.config = self._load_config()
    
    def _setup_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        for directory in [self.DATA_DIR, self.REPORTS_DIR, self.BACKUP_DIR]:
            directory.mkdir(exist_ok=True)
    
    def _load_data(self) -> pd.DataFrame:
        """Load expense data from CSV file with error handling."""
        try:
            if self.DATA_FILE.exists():
                df = pd.read_csv(self.DATA_FILE)
                df['Date'] = pd.to_datetime(df['Date'])
                return df
            else:
                return pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount', 'ID'])
        except Exception as e:
            print(f"⚠️ Error loading data: {e}")
            print("Creating new data file...")
            return pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount', 'ID'])
    
    def _load_config(self) -> Dict:
        """Load user configuration settings."""
        default_config = {
            'currency_symbol': '₹',
            'monthly_budget': None,
            'date_format': '%Y-%m-%d'
        }
        
        try:
            if self.CONFIG_FILE.exists():
                with open(self.CONFIG_FILE, 'r') as f:
                    return {**default_config, **json.load(f)}
        except Exception as e:
            print(f"⚠️ Error loading config: {e}")
        
        return default_config
    
    def _save_config(self) -> None:
        """Save configuration settings to file."""
        try:
            with open(self.CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"⚠️ Error saving config: {e}")
    
    def _save_data(self) -> bool:
        """Save expense data to CSV with backup."""
        try:
            # Create backup before saving
            if self.DATA_FILE.exists():
                backup_name = f"expenses_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                shutil.copy2(self.DATA_FILE, self.BACKUP_DIR / backup_name)
                
                # Keep only last 5 backups
                backups = sorted(self.BACKUP_DIR.glob('expenses_backup_*.csv'))
                for old_backup in backups[:-5]:
                    old_backup.unlink()
            
            # Save current data
            self.df.to_csv(self.DATA_FILE, index=False)
            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def _generate_id(self) -> str:
        """Generate a unique ID for new expense entries."""
        if self.df.empty:
            return "EXP001"
        
        last_id = self.df['ID'].max()
        if pd.isna(last_id):
            return "EXP001"
        
        try:
            num = int(last_id.replace('EXP', '')) + 1
            return f"EXP{num:03d}"
        except:
            return f"EXP{len(self.df) + 1:03d}"
    
    def _validate_date(self, date_str: str) -> Optional[datetime]:
        """Validate and parse date string."""
        if not date_str.strip():
            return datetime.today()
        
        try:
            return datetime.strptime(date_str, self.config['date_format'])
        except ValueError:
            print(f"❌ Invalid date format. Please use {self.config['date_format']}")
            return None
    
    def _validate_amount(self, amount_str: str) -> Optional[float]:
        """Validate amount input."""
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("❌ Amount must be positive!")
                return None
            if amount > 1000000:
                print("❌ Amount seems unusually large. Please verify.")
                confirm = input("Continue anyway? (yes/no): ").strip().lower()
                if confirm != 'yes':
                    return None
            return amount
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
            return None
    
    def _select_category(self) -> Optional[str]:
        """Display category menu and get user selection."""
        print("\n📋 Available Categories:")
        for idx, cat in enumerate(self.CATEGORIES, 1):
            print(f"  {idx}. {cat}")
        
        try:
            choice = input(f"\nSelect category (1-{len(self.CATEGORIES)}): ").strip()
            idx = int(choice) - 1
            if 0 <= idx < len(self.CATEGORIES):
                return self.CATEGORIES[idx]
            else:
                print("❌ Invalid selection!")
                return None
        except ValueError:
            print("❌ Please enter a number!")
            return None
    
    def add_expense(self) -> None:
        """Add a new expense with comprehensive validation."""
        print("\n" + "="*50)
        print("🧾 Add New Expense")
        print("="*50)
        
        # Get and validate date
        date_input = input(f"Enter date ({self.config['date_format']}) [blank for today]: ").strip()
        date_obj = self._validate_date(date_input)
        if date_obj is None:
            return
        
        # Get description
        description = input("Enter description: ").strip()
        if not description:
            print("❌ Description cannot be empty!")
            return
        
        # Get category
        category = self._select_category()
        if category is None:
            return
        
        # Get and validate amount
        amount_input = input(f"Enter amount ({self.config['currency_symbol']}): ").strip()
        amount = self._validate_amount(amount_input)
        if amount is None:
            return
        
        # Create new entry
        expense_id = self._generate_id()
        new_entry = pd.DataFrame([{
            'Date': date_obj,
            'Description': description,
            'Category': category,
            'Amount': amount,
            'ID': expense_id
        }])
        
        self.df = pd.concat([self.df, new_entry], ignore_index=True)
        
        if self._save_data():
            print(f"\n✅ Expense added successfully! (ID: {expense_id})")
            
            # Check budget warning
            if self.config['monthly_budget']:
                month_total = self._get_current_month_total()
                if month_total > self.config['monthly_budget']:
                    print(f"⚠️ WARNING: You've exceeded your monthly budget!")
                    print(f"Budget: {self.config['currency_symbol']}{self.config['monthly_budget']:,.2f}")
                    print(f"Spent: {self.config['currency_symbol']}{month_total:,.2f}")
        else:
            print("❌ Failed to save expense!")
    
    def _get_current_month_total(self) -> float:
        """Calculate total expenses for current month."""
        if self.df.empty:
            return 0.0
        
        current_month = datetime.now().to_period('M')
        monthly_data = self.df[self.df['Date'].dt.to_period('M') == current_month]
        return monthly_data['Amount'].sum()
    
    def view_expenses(self) -> None:
        """View all expenses with filtering options."""
        if self.df.empty:
            print("\n⚠️ No expenses recorded yet!")
            return
        
        print("\n" + "="*50)
        print("📋 View Expenses")
        print("="*50)
        print("1. View All")
        print("2. Filter by Date Range")
        print("3. Filter by Category")
        print("4. Search by Description")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        filtered_df = self.df.copy()
        
        if choice == '2':
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            try:
                start_date = pd.to_datetime(start)
                end_date = pd.to_datetime(end)
                filtered_df = filtered_df[
                    (filtered_df['Date'] >= start_date) & 
                    (filtered_df['Date'] <= end_date)
                ]
            except:
                print("❌ Invalid date format!")
                return
        
        elif choice == '3':
            category = self._select_category()
            if category:
                filtered_df = filtered_df[filtered_df['Category'] == category]
        
        elif choice == '4':
            search_term = input("Enter search term: ").strip().lower()
            filtered_df = filtered_df[
                filtered_df['Description'].str.lower().str.contains(search_term)
            ]
        
        if filtered_df.empty:
            print("\n⚠️ No expenses found matching your criteria!")
            return
        
        # Display results
        print(f"\n📊 Found {len(filtered_df)} expense(s):")
        print("-" * 100)
        
        display_df = filtered_df.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
        display_df['Amount'] = display_df['Amount'].apply(
            lambda x: f"{self.config['currency_symbol']}{x:,.2f}"
        )
        
        print(display_df.to_string(index=False))
        print("-" * 100)
        print(f"Total: {self.config['currency_symbol']}{filtered_df['Amount'].sum():,.2f}")
    
    def edit_expense(self) -> None:
        """Edit an existing expense."""
        if self.df.empty:
            print("\n⚠️ No expenses to edit!")
            return
        
        print("\n" + "="*50)
        print("✏️ Edit Expense")
        print("="*50)
        
        expense_id = input("Enter expense ID to edit: ").strip().upper()
        
        if expense_id not in self.df['ID'].values:
            print(f"❌ Expense ID '{expense_id}' not found!")
            return
        
        # Show current expense
        idx = self.df[self.df['ID'] == expense_id].index[0]
        current = self.df.loc[idx]
        
        print(f"\nCurrent expense details:")
        print(f"Date: {current['Date'].strftime('%Y-%m-%d')}")
        print(f"Description: {current['Description']}")
        print(f"Category: {current['Category']}")
        print(f"Amount: {self.config['currency_symbol']}{current['Amount']:,.2f}")
        
        print("\nWhat would you like to edit?")
        print("1. Date")
        print("2. Description")
        print("3. Category")
        print("4. Amount")
        print("5. Cancel")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            date_input = input(f"New date ({self.config['date_format']}): ").strip()
            date_obj = self._validate_date(date_input)
            if date_obj:
                self.df.at[idx, 'Date'] = date_obj
        
        elif choice == '2':
            description = input("New description: ").strip()
            if description:
                self.df.at[idx, 'Description'] = description
        
        elif choice == '3':
            category = self._select_category()
            if category:
                self.df.at[idx, 'Category'] = category
        
        elif choice == '4':
            amount_input = input(f"New amount ({self.config['currency_symbol']}): ").strip()
            amount = self._validate_amount(amount_input)
            if amount:
                self.df.at[idx, 'Amount'] = amount
        
        elif choice == '5':
            print("Edit cancelled.")
            return
        
        else:
            print("❌ Invalid choice!")
            return
        
        if self._save_data():
            print("✅ Expense updated successfully!")
        else:
            print("❌ Failed to update expense!")
    
    def delete_expense(self) -> None:
        """Delete an expense with confirmation."""
        if self.df.empty:
            print("\n⚠️ No expenses to delete!")
            return
        
        print("\n" + "="*50)
        print("🗑️ Delete Expense")
        print("="*50)
        
        expense_id = input("Enter expense ID to delete: ").strip().upper()
        
        if expense_id not in self.df['ID'].values:
            print(f"❌ Expense ID '{expense_id}' not found!")
            return
        
        # Show expense to be deleted
        expense = self.df[self.df['ID'] == expense_id].iloc[0]
        print(f"\nExpense to delete:")
        print(f"ID: {expense['ID']}")
        print(f"Date: {expense['Date'].strftime('%Y-%m-%d')}")
        print(f"Description: {expense['Description']}")
        print(f"Category: {expense['Category']}")
        print(f"Amount: {self.config['currency_symbol']}{expense['Amount']:,.2f}")
        
        confirm = input("\n⚠️ Are you sure you want to delete this expense? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            self.df = self.df[self.df['ID'] != expense_id]
            if self._save_data():
                print("✅ Expense deleted successfully!")
            else:
                print("❌ Failed to delete expense!")
        else:
            print("Deletion cancelled.")
    
    def show_summary(self) -> None:
        """Display comprehensive expense statistics."""
        if self.df.empty:
            print("\n⚠️ No expense data found. Add some expenses first!")
            return
        
        print("\n" + "="*70)
        print("📊 EXPENSE SUMMARY")
        print("="*70)
        
        # Overall statistics
        total_spent = self.df['Amount'].sum()
        avg_expense = self.df['Amount'].mean()
        max_expense = self.df['Amount'].max()
        expense_count = len(self.df)
        
        print(f"\n💰 Overall Statistics:")
        print(f"  Total Spent:        {self.config['currency_symbol']}{total_spent:,.2f}")
        print(f"  Average Expense:    {self.config['currency_symbol']}{avg_expense:,.2f}")
        print(f"  Largest Expense:    {self.config['currency_symbol']}{max_expense:,.2f}")
        print(f"  Number of Expenses: {expense_count}")
        
        # Monthly budget status
        if self.config['monthly_budget']:
            month_total = self._get_current_month_total()
            remaining = self.config['monthly_budget'] - month_total
            print(f"\n📅 Current Month Budget:")
            print(f"  Budget:    {self.config['currency_symbol']}{self.config['monthly_budget']:,.2f}")
            print(f"  Spent:     {self.config['currency_symbol']}{month_total:,.2f}")
            print(f"  Remaining: {self.config['currency_symbol']}{remaining:,.2f}")
            
            if remaining < 0:
                print(f"  ⚠️ OVER BUDGET by {self.config['currency_symbol']}{abs(remaining):,.2f}")
        
        # Category breakdown
        by_category = self.df.groupby('Category')['Amount'].agg(['sum', 'count']).sort_values('sum', ascending=False)
        print(f"\n📋 Spending by Category:")
        print("-" * 70)
        for cat, row in by_category.iterrows():
            percentage = (row['sum'] / total_spent) * 100
            print(f"  {cat:<20} {self.config['currency_symbol']}{row['sum']:>10,.2f}  ({int(row['count'])} items)  [{percentage:>5.1f}%]")
        
        # Monthly trends
        by_month = self.df.groupby(self.df['Date'].dt.to_period('M'))['Amount'].sum().tail(6)
        if len(by_month) > 0:
            print(f"\n📅 Monthly Spending (Last 6 Months):")
            print("-" * 70)
            for month, amount in by_month.items():
                print(f"  {str(month):<15} {self.config['currency_symbol']}{amount:>10,.2f}")
        
        # Top 5 expenses
        top_5 = self.df.nlargest(5, 'Amount')[['Date', 'Description', 'Category', 'Amount']]
        if not top_5.empty:
            print(f"\n🔝 Top 5 Largest Expenses:")
            print("-" * 70)
            for _, expense in top_5.iterrows():
                print(f"  {expense['Date'].strftime('%Y-%m-%d')}  {expense['Description']:<25} {expense['Category']:<20} {self.config['currency_symbol']}{expense['Amount']:>8,.2f}")
        
        # Save report
        try:
            summary_data = {
                'Category': by_category.index,
                'Total_Spent': by_category['sum'].values,
                'Count': by_category['count'].values,
                'Percentage': (by_category['sum'].values / total_spent * 100)
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_csv(self.REPORT_FILE, index=False)
            print(f"\n💾 Summary report saved to '{self.REPORT_FILE}'")
        except Exception as e:
            print(f"⚠️ Could not save report: {e}")
    
    def visualize_data(self) -> None:
        """Create comprehensive visualizations of expense data."""
        if self.df.empty:
            print("\n⚠️ No data to visualize. Add some expenses first!")
            return
        
        print("\n📈 Generating visualizations...")
        
        # Prepare data
        by_category = self.df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        by_month = self.df.groupby(self.df['Date'].dt.to_period('M'))['Amount'].sum()
        
        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('💰 Expense Analysis Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Pie Chart - Category Distribution
        colors = plt.cm.Set3(range(len(by_category)))
        axes[0, 0].pie(by_category, labels=by_category.index, autopct='%1.1f%%', 
                       startangle=140, colors=colors)
        axes[0, 0].set_title('Spending by Category')
        
        # 2. Bar Chart - Category Totals
        by_category.plot(kind='barh', ax=axes[0, 1], color='steelblue')
        axes[0, 1].set_title('Category-wise Spending')
        axes[0, 1].set_xlabel(f'Amount ({self.config["currency_symbol"]})')
        axes[0, 1].grid(axis='x', linestyle='--', alpha=0.6)
        
        # 3. Line Chart - Monthly Trend
        by_month.plot(kind='line', ax=axes[1, 0], marker='o', color='mediumseagreen', linewidth=2)
        axes[1, 0].set_title('Monthly Spending Trend')
        axes[1, 0].set_xlabel('Month')
        axes[1, 0].set_ylabel(f'Amount ({self.config["currency_symbol"]})')
        axes[1, 0].grid(True, linestyle='--', alpha=0.6)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 4. Bar Chart - Monthly Spending
        by_month.plot(kind='bar', ax=axes[1, 1], color='coral')
        axes[1, 1].set_title('Monthly Spending Distribution')
        axes[1, 1].set_xlabel('Month')
        axes[1, 1].set_ylabel(f'Amount ({self.config["currency_symbol"]})')
        axes[1, 1].grid(axis='y', linestyle='--', alpha=0.6)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        # Save figure
        try:
            chart_file = self.REPORTS_DIR / f'expense_charts_{datetime.now().strftime("%Y%m%d")}.png'
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            print(f"💾 Charts saved to '{chart_file}'")
        except Exception as e:
            print(f"⚠️ Could not save charts: {e}")
        
        plt.show()
    
    def set_budget(self) -> None:
        """Set or update monthly budget."""
        print("\n" + "="*50)
        print("💵 Set Monthly Budget")
        print("="*50)
        
        current_budget = self.config.get('monthly_budget')
        if current_budget:
            print(f"Current budget: {self.config['currency_symbol']}{current_budget:,.2f}")
        else:
            print("No budget set currently.")
        
        budget_input = input(f"\nEnter monthly budget ({self.config['currency_symbol']}) [0 to disable]: ").strip()
        
        budget = self._validate_amount(budget_input) if budget_input != '0' else 0
        
        if budget is not None:
            self.config['monthly_budget'] = budget if budget > 0 else None
            self._save_config()
            
            if budget > 0:
                print(f"✅ Monthly budget set to {self.config['currency_symbol']}{budget:,.2f}")
            else:
                print("✅ Monthly budget disabled")
    
    def export_data(self) -> None:
        """Export data in various formats."""
        if self.df.empty:
            print("\n⚠️ No data to export!")
            return
        
        print("\n" + "="*50)
        print("📤 Export Data")
        print("="*50)
        print("1. CSV (Current format)")
        print("2. Excel (.xlsx)")
        print("3. JSON")
        
        choice = input("\nSelect format (1-3): ").strip()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        try:
            if choice == '1':
                filename = self.REPORTS_DIR / f'expenses_export_{timestamp}.csv'
                self.df.to_csv(filename, index=False)
            
            elif choice == '2':
                filename = self.REPORTS_DIR / f'expenses_export_{timestamp}.xlsx'
                self.df.to_excel(filename, index=False, engine='openpyxl')
            
            elif choice == '3':
                filename = self.REPORTS_DIR / f'expenses_export_{timestamp}.json'
                export_df = self.df.copy()
                export_df['Date'] = export_df['Date'].dt.strftime('%Y-%m-%d')
                export_df.to_json(filename, orient='records', indent=2)
            
            else:
                print("❌ Invalid choice!")
                return
            
            print(f"✅ Data exported successfully to '{filename}'")
        
        except Exception as e:
            print(f"❌ Export failed: {e}")
    
    def run(self) -> None:
        """Main application loop."""
        print("\n" + "="*60)
        print("💸 Welcome to Personal Expense Tracker - Professional Edition")
        print("="*60)
        
        while True:
            print("\n" + "="*60)
            print("MAIN MENU")
            print("="*60)
            print("1️⃣   Add New Expense")
            print("2️⃣   View Expenses")
            print("3️⃣   Edit Expense")
            print("4️⃣   Delete Expense")
            print("5️⃣   Show Summary")
            print("6️⃣   Visualize Data")
            print("7️⃣   Set Monthly Budget")
            print("8️⃣   Export Data")
            print("9️⃣   Exit")
            print("-" * 60)
            
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.edit_expense()
            elif choice == '4':
                self.delete_expense()
            elif choice == '5':
                self.show_summary()
            elif choice == '6':
                self.visualize_data()
            elif choice == '7':
                self.set_budget()
            elif choice == '8':
                self.export_data()
            elif choice == '9':
                print("\n" + "="*60)
                print("👋 Thank you for using Expense Tracker!")
                print("💡 Remember: Smart spending leads to financial freedom!")
                print("="*60 + "\n")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1-9.")
            
            input("\nPress Enter to continue...")


def main():
    """Entry point for the application."""
    try:
        tracker = ExpenseTracker()
        tracker.run()
    except KeyboardInterrupt:
        print("\n\n⚠️ Application interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please check your data files and try again.")


if __name__ == "__main__":
    main()