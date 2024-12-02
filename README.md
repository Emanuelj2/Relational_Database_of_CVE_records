# Relational_Database_of_CVE_records
The system aids in evaluating the security of major RDBMS and their versions. It simplifies decision-making but is not a replacement for independent research. Designed as a supplementary tool, it provides quick insights and rankings, ideal for initial evaluations when used alongside additional resources

This project is a Python-based data analysis and visualization tool for exploring CVSS scores from vulnerability datasets. It integrates a GUI application using Tkinter and provides data visualizations for better insights into the severity of vulnerabilities across different database products.

# Features
-  Login System:
   -  Secure login system for authentication (login.py).
-  Graphical User Interface:
    -  Intuitive UI built with Tkinter for navigating and interacting with data (GUI.py).
-  Data Analysis:
    -  Merges and processes data from CSV files to generate:
    -  Histograms of CVSS scores by product group.
    -  Pie charts of average CVSS scores by product group (analyze_data.py).
-  Customizable Visualizations:
    -  Allows for tailored data exploration through real-time visualizations.
   
# Prerequisites
### IDE's
-  vscode (https://code.visualstudio.com/download)
-  pycharm (https://www.jetbrains.com/pycharm/)
-  Python 3.8 or above
### DataBase server
-  MySQL Workbench (https://www.mysql.com/products/workbench/)
-  https://youtu.be/wgRwITQHszU?si=s4Nv8-L5PVFR6lw1 (Use Full)
-  https://youtu.be/ftlJoXEBmis?si=r3KPkbS4TtEyo92t
### Libraries
``` bash
pip install mysql-connector-python pandas matplotlib tabulate
```
# File Structure
```
.
├── login.py             # Handles user authentication
├── GUI.py               # Main Tkinter application
├── analyze_data.py      # Data analysis and visualization logic
├── Products.csv         # CSV file containing product information
├── CVE_RECORDS2.csv     # CSV file containing CVE records
└── README.md            # This README file
```
# Configuration
### database connection
-   In the GUI.py file there is a code simmilar to the one below, uodate the following database cradentials to successfuly connect 
```python
DB_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database'
}
```
# Usage
### Running the Application
```bash
python login_page.py
```
-  Use the dropdown menus to select tables and columns for data display.
-  Use the buttons to:
      -  fetch sorted data
      -  Display natrual join results
      -  Generate histograms and pie charts
### Visualization
-  Histograms and pie charts are displayed in separate windows. They are based on the data loaded from the merged tables or the database.

# Contribution
-  Pierson Alexander
-  Emanuel Jose
-  Amanda Rodriguez
