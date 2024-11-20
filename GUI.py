
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Database connection configuration (replace with your actual DB credentials)
DB_CONFIG = {
    'user': 'root',
    'password': 'Pass-white28',
    'host': '127.0.0.1',
    'database': 'MYDB1'
}

# Function to fetch tables from the database
def fetch_tables(table_dropdown, table2_dropdown):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
        table_dropdown["values"] = table_names  # Update dropdown values
        table2_dropdown["values"] = table_names  # Same for second table dropdown
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        print(f"Error: {err}")

# Function to fetch data based on the selected table and conditions
def fetch_sorted_data(table_dropdown, sort_column_combobox, sort_order_combobox, tree):
    table_name = table_dropdown.get()
    sort_column = sort_column_combobox.get()
    sort_order = sort_order_combobox.get()

    if not table_name or not sort_column or not sort_order:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name} ORDER BY {sort_column} {sort_order}"
        print(f"Executing query: {query}")  # Debugging line
        cursor.execute(query)
        data = cursor.fetchall()

        # Clear the table before inserting new data
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the table
        for row in data:
            tree.insert("", "end", values=row)

        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        print(f"Error: {err}")

# Function to fetch data with a natural join between two tables
def fetch_natural_join_data(table_dropdown, table2_dropdown, tree):
    table1 = table_dropdown.get()
    table2 = table2_dropdown.get()

    if not table1 or not table2:
        messagebox.showwarning("Input Error", "Please select both tables.")
        return

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = f"SELECT * FROM {table1} NATURAL JOIN {table2}"
        print(f"Executing query: {query}")  # Debugging line
        cursor.execute(query)
        data = cursor.fetchall()

        # Clear the table before inserting new data
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the table
        for row in data:
            tree.insert("", "end", values=row)

        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        print(f"Error: {err}")

# Function to open the main GUI window (called after successful login)
def open_gui():
    # Create the main window for the fetcher
    fetcher_window = tk.Tk()
    fetcher_window.title("Database Fetcher")

    # Create input frame
    input_frame = ttk.Frame(fetcher_window)
    input_frame.pack(padx=10, pady=10)

    # Table selection dropdown
    tk.Label(input_frame, text="Select Table:").grid(row=0, column=0, padx=10, pady=5)
    table_dropdown = ttk.Combobox(input_frame)
    table_dropdown.grid(row=0, column=1, padx=10, pady=5)

    # Table selection for natural join
    tk.Label(input_frame, text="Select Second Table (for Natural Join):").grid(row=1, column=0, padx=10, pady=5)
    table2_dropdown = ttk.Combobox(input_frame)
    table2_dropdown.grid(row=1, column=1, padx=10, pady=5)

    # Sorting options
    tk.Label(input_frame, text="Sort by Column:").grid(row=2, column=0, padx=10, pady=5)
    sort_column_combobox = ttk.Combobox(input_frame, values=["cvss_score", "published_date", "last_modified"])
    sort_column_combobox.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Sort Order:").grid(row=3, column=0, padx=10, pady=5)
    sort_order_combobox = ttk.Combobox(input_frame, values=["ASC", "DESC"])
    sort_order_combobox.grid(row=3, column=1, padx=10, pady=5)

    # Buttons
    fetch_button = ttk.Button(input_frame, text="Fetch Sorted Data", command=lambda: fetch_sorted_data(table_dropdown, sort_column_combobox, sort_order_combobox, tree))
    fetch_button.grid(row=4, column=0, pady=10)

    join_button = ttk.Button(input_frame, text="Fetch Natural Join Data", command=lambda: fetch_natural_join_data(table_dropdown, table2_dropdown, tree))
    join_button.grid(row=4, column=1, pady=10)

    # Table to display fetched data
    tree = ttk.Treeview(fetcher_window, show="headings")
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Fetch tables and update dropdowns
    fetch_tables(table_dropdown, table2_dropdown)

    # Run the fetcher window
    fetcher_window.mainloop()
