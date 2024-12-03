import tkinter as tk
from tkinter import messagebox
import GUI  # Import the GUI file with the open_gui function

# Dummy user data for validation (you can replace this with actual DB validation)
USER_CREDENTIALS = {"username": "admin", "password": "12345"}


# Function to validate login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the credentials match
    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        messagebox.showinfo("Login Success", "Welcome!")
        root.quit()  # Close the login window
        GUI.open_gui()  # Call the open_gui function from GUI.py to open the main application
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Create the login window
root = tk.Tk()
root.title("Login Page")

# Create and place labels and entry fields for username and password
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")  # Hides the password with asterisks
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the login window
root.mainloop()
