# 💰 Personal Expense Tracker - Professional Edition

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen)

**A powerful, production-ready command-line application for tracking and analyzing personal expenses with advanced features.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Technologies](#-technologies)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

Personal Expense Tracker Pro is a comprehensive Python application designed to help you take control of your finances. With features like automatic backups, budget tracking, data visualization, and multiple export formats, it's perfect for anyone looking to manage their expenses professionally.

### Why Use This Tracker?

- 🎨 **User-Friendly**: Intuitive command-line interface with clear prompts
- 🔒 **Data Safety**: Automatic backups ensure you never lose your data
- 📊 **Visual Insights**: Beautiful charts to understand spending patterns
- 💵 **Budget Control**: Set limits and get real-time warnings
- 🔍 **Powerful Search**: Find expenses by date, category, or description
- 📤 **Flexible Export**: Export to CSV, Excel, or JSON formats
- ✅ **Production-Ready**: Professional code with error handling and validation

---

## ✨ Features

### Core Functionality
- ✅ **Complete CRUD Operations**: Add, view, edit, and delete expenses
- 🆔 **Unique ID System**: Every expense gets a trackable ID (EXP001, EXP002, etc.)
- 📋 **Standardized Categories**: 9 predefined categories to maintain consistency
- 📅 **Smart Date Handling**: Auto-fills today's date or accepts custom dates
- 💰 **Amount Validation**: Prevents invalid entries and warns about large amounts

### Advanced Features
- 📊 **Comprehensive Statistics**: 
  - Total spending, average expense, largest expense
  - Category-wise breakdown with percentages
  - Monthly trends analysis
  - Top 5 largest expenses
  
- 📈 **Data Visualization**:
  - Category distribution (Pie Chart)
  - Category totals (Horizontal Bar Chart)
  - Monthly trends (Line Chart)
  - Monthly distribution (Bar Chart)
  
- 🔍 **Smart Filtering**:
  - Filter by date range
  - Filter by category
  - Search by description keywords
  
- 💵 **Budget Management**:
  - Set monthly budget limits
  - Real-time budget tracking
  - Instant warnings when exceeding budget
  
- 💾 **Data Management**:
  - Automatic backups before every save
  - Keeps last 5 backups with timestamps
  - Export to CSV, Excel (.xlsx), or JSON
  - Configuration persistence

### Safety & Reliability
- 🔒 **Error Handling**: Comprehensive validation and error recovery
- 💾 **Auto-Backups**: Never lose data with automatic backup rotation
- ✅ **Input Validation**: All inputs are validated before processing
- ⚠️ **Confirmation Prompts**: Destructive actions require confirmation
- 🛡️ **Data Integrity**: Safe file operations prevent corruption

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker-pro.git
cd expense-tracker-pro
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `pandas` - Data manipulation and analysis
- `matplotlib` - Data visualization
- `openpyxl` - Excel file support

### Step 3: Run the Application

```bash
python expense_tracker.py
```

---

## ⚡ Quick Start

### First Time Setup

1. **Run the application**:
   ```bash
   python expense_tracker.py
   ```

2. **Add your first expense**:
   - Select option `1` from the menu
   - Press Enter for today's date or enter a custom date
   - Enter description (e.g., "Lunch at Cafe")
   - Select category from the list
   - Enter amount

3. **Set a monthly budget** (optional):
   - Select option `7`
   - Enter your monthly budget limit

4. **Start tracking!** The app will automatically:
   - Create necessary folders (`data/`, `reports/`, `backups/`)
   - Save your expenses
   - Create backups
   - Warn you when approaching budget limits

---

## 📚 Usage Guide

### Main Menu Options

```
1️⃣  Add New Expense       - Record a new expense
2️⃣  View Expenses         - View and filter expenses
3️⃣  Edit Expense          - Modify existing expense
4️⃣  Delete Expense        - Remove an expense
5️⃣  Show Summary          - View detailed statistics
6️⃣  Visualize Data        - Generate charts and graphs
7️⃣  Set Monthly Budget    - Configure spending limits
8️⃣  Export Data           - Export to CSV/Excel/JSON
9️⃣  Exit                  - Close application
```

### 1. Adding an Expense

```
📋 Available Categories:
  1. Food & Dining
  2. Transportation
  3. Entertainment
  4. Shopping
  5. Bills & Utilities
  6. Healthcare
  7. Education
  8. Groceries
  9. Other
```

**Example:**
```
Enter date (YYYY-MM-DD) [blank for today]: 
Enter description: Coffee at Starbucks
Select category (1-9): 1
Enter amount (₹): 250
✅ Expense added successfully! (ID: EXP001)
```

### 2. Viewing Expenses

**Filter Options:**
- View all expenses
- Filter by date range (e.g., 2024-01-01 to 2024-01-31)
- Filter by category
- Search by description keywords

**Example Output:**
```
📊 Found 5 expense(s):
────────────────────────────────────────────────────────────────────
Date       Description              Category        Amount      ID
2024-01-06 Coffee at Starbucks     Food & Dining   ₹250.00    EXP001
2024-01-05 Uber Ride               Transportation  ₹180.00    EXP002
────────────────────────────────────────────────────────────────────
Total: ₹430.00
```

### 3. Editing an Expense

- Enter the expense ID (e.g., EXP001)
- Select what to edit: Date, Description, Category, or Amount
- Enter new value
- Changes are saved with automatic backup

### 4. Summary Statistics

**Displays:**
- Overall statistics (total spent, average, largest expense)
- Current month budget status
- Category breakdown with percentages and item counts
- Monthly trends (last 6 months)
- Top 5 largest expenses
- Auto-generates CSV report

**Example Output:**
```
📊 EXPENSE SUMMARY
══════════════════════════════════════════════════════════════════════

💰 Overall Statistics:
  Total Spent:        ₹15,450.00
  Average Expense:    ₹515.00
  Largest Expense:    ₹2,500.00
  Number of Expenses: 30

📅 Current Month Budget:
  Budget:    ₹20,000.00
  Spent:     ₹8,500.00
  Remaining: ₹11,500.00

📋 Spending by Category:
──────────────────────────────────────────────────────────────────────
  Food & Dining        ₹5,200.00  (12 items)  [33.7%]
  Transportation       ₹3,800.00  (8 items)   [24.6%]
  Entertainment        ₹2,450.00  (5 items)   [15.9%]
```

### 5. Data Visualization

Generates a comprehensive dashboard with 4 charts:
- **Pie Chart**: Category distribution
- **Horizontal Bar**: Category totals
- **Line Chart**: Monthly spending trend
- **Bar Chart**: Monthly distribution

Charts are displayed on screen and saved as PNG files in the `reports/` folder.

### 6. Budget Management

Set a monthly budget to track your spending:
```
💵 Set Monthly Budget
Enter monthly budget (₹): 20000
✅ Monthly budget set to ₹20,000.00
```

**Features:**
- Real-time tracking of current month spending
- Warnings when exceeding budget
- Budget status shown in summary
- Can be disabled by setting to 0

### 7. Export Options

Export your data in multiple formats:
- **CSV**: Compatible with Excel and Google Sheets
- **Excel (.xlsx)**: Formatted spreadsheet with formulas
- **JSON**: For programmatic access or web apps

Exported files include timestamp and are saved in `reports/` folder.

---

## 📁 Project Structure

```
expense-tracker-pro/
│
├── expense_tracker.py          # Main application file
│
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── .gitignore                 # Git ignore rules
│
├── data/                       # Auto-created on first run
│   ├── expenses.csv           # Main expense database
│   └── config.json            # User configuration
│
├── reports/                    # Auto-created on first run
│   ├── summary_report.csv     # Latest summary report
│   ├── expense_charts_*.png   # Generated visualizations
│   └── expenses_export_*.xlsx # Exported data files
│
└── backups/                    # Auto-created on first run
    ├── expenses_backup_20240106_143022.csv
    ├── expenses_backup_20240106_143145.csv
    └── ... (last 5 backups kept)
```

### Key Files

- **expense_tracker.py**: The main application containing all functionality
- **expenses.csv**: Your expense database (automatically backed up)
- **config.json**: Stores settings like budget and preferences
- **summary_report.csv**: Latest expense summary report
- **Backup files**: Automatic timestamped backups

---

## 🛠️ Technologies

### Core Technologies
- **Python 3.8+**: Main programming language
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization and charting

### Additional Libraries
- **pathlib**: Cross-platform file path handling
- **json**: Configuration management
- **datetime**: Date and time operations
- **shutil**: File operations and backups

### Architecture
- **Object-Oriented Design**: Clean class-based structure
- **Type Hints**: Better code documentation and IDE support
- **Error Handling**: Comprehensive try-except blocks
- **Data Validation**: Input validation at every step

---

## 📸 Screenshots

### Main Menu
```
══════════════════════════════════════════════════════════════
MAIN MENU
══════════════════════════════════════════════════════════════
1️⃣   Add New Expense
2️⃣   View Expenses
3️⃣   Edit Expense
4️⃣   Delete Expense
5️⃣   Show Summary
6️⃣   Visualize Data
7️⃣   Set Monthly Budget
8️⃣   Export Data
9️⃣   Exit
────────────────────────────────────────────────────────────────
Enter your choice (1-9):
```

### Adding an Expense
```
══════════════════════════════════════════════════════
🧾 Add New Expense
══════════════════════════════════════════════════════
Enter date (YYYY-MM-DD) [blank for today]: 
Enter description: Lunch at McDonald's
Select category (1-9): 1
Enter amount (₹): 450

✅ Expense added successfully! (ID: EXP025)
```

### Budget Warning
```
⚠️ WARNING: You've exceeded your monthly budget!
Budget: ₹20,000.00
Spent: ₹21,450.00
```

---

## 🎨 Customization

### Modify Categories

Edit the `CATEGORIES` list in the `ExpenseTracker` class:

```python
CATEGORIES = [
    'Food & Dining',
    'Transportation',
    'Your Custom Category',  # Add your own
    # ... more categories
]
```

### Change Currency Symbol

Modify the default config in `_load_config()` method:

```python
default_config = {
    'currency_symbol': '$',  # Change from ₹ to $
    'monthly_budget': None,
    'date_format': '%Y-%m-%d'
}
```

### Adjust Backup Retention

Change the number of backups to keep in `_save_data()` method:

```python
# Keep only last 10 backups instead of 5
for old_backup in backups[:-10]:
    old_backup.unlink()
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
4. **Commit with clear messages**:
   ```bash
   git commit -m "Add: Amazing new feature"
   ```
5. **Push to your branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Contribution Ideas

- 🌍 Multi-currency support
- 📱 Mobile-friendly web interface
- 🔔 Notification system for budget alerts
- 📧 Email reports
- 🔗 Bank account integration
- 🎯 Savings goals tracker
- 📊 More visualization options
- 🌙 Dark mode for visualizations
- 🗂️ Multiple user profiles
- ☁️ Cloud sync capabilities

### Code Style

- Follow PEP 8 guidelines
- Add type hints to new functions
- Include docstrings for classes and methods
- Write comprehensive error handling
- Add comments for complex logic

---

## 🐛 Known Issues & Roadmap

### Current Limitations
- Command-line only (no GUI)
- Single-user system
- No cloud synchronization
- Limited to local file storage

### Future Enhancements
- [ ] Web-based interface using Flask/Django
- [ ] Mobile app version
- [ ] Cloud backup integration
- [ ] Recurring expense support
- [ ] Receipt image attachment
- [ ] Multi-currency support
- [ ] Expense sharing between users
- [ ] Budget recommendations using ML
- [ ] Integration with banking APIs
- [ ] Tax report generation

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 [Dhairya Singh Dhaila]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 💬 Support

### Getting Help

- 📧 **Email**: dhairya.dhaila@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/ch4lkp0wd3r/expense-tracker-pro/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/ch4lkp0wd3r/expense-tracker-pro/discussions)

### FAQ

**Q: Where is my data stored?**  
A: All data is stored locally in the `data/` folder as CSV files. Backups are in the `backups/` folder.

**Q: Can I recover deleted expenses?**  
A: Yes! Check the `backups/` folder for previous versions of your expense database.

**Q: How do I reset everything?**  
A: Delete the `data/`, `reports/`, and `backups/` folders. The app will recreate them on next run.

**Q: Can multiple people use this?**  
A: Currently, it's designed for single-user use. Multi-user support is on the roadmap.

**Q: Is my data secure?**  
A: Data is stored locally on your computer. Make sure to backup important files and keep your computer secure.

---

## 🌟 Acknowledgments

- **pandas** team for the excellent data manipulation library
- **matplotlib** developers for powerful visualization tools
- Python community for continuous support and resources
- All contributors who help improve this project

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/expense-tracker-pro?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/expense-tracker-pro?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/YOUR_USERNAME/expense-tracker-pro?style=social)

---

<div align="center">

**Made with ❤️ and Python**

If you found this project helpful, please consider giving it a ⭐!

[⬆ Back to Top](#-personal-expense-tracker---professional-edition)

</div>