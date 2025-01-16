import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create the main application window
app = tk.Tk()
app.title("Tkinter Application x Database Integration")

# Database setup
connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER
                    )''')
    connection.commit()

'''
# Function to clear the table in the database
def clear_table():
    cursor.execute("DELETE FROM people")
    connection.commit()
    messagebox.showinfo("Success", "Table cleared successfully!")
'''

# Function to insert data into the database
def insert_data():
    name = name_entry.get()
    age = age_entry.get()

    if name and age:
        cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
        connection.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
    else:
        messagebox.showerror("Error", "Please enter both Name and Age.")

# Function to fetch data from the database
def fetch_data():
    cursor.execute("SELECT * FROM people")
    data = cursor.fetchall()

    if data:
        # Display data in a new window or widget
        # For simplicity, let's just print the data in the console
        for record in data:
            print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")
    else:
        messagebox.showinfo("Info", "No data found.")

# Function to update data in the database
def update_data():
    user_id = id_entry.get()

    if user_id:
        new_name = name_entry.get()
        new_age = age_entry.get()
        cursor.execute("UPDATE people SET name=?, age=? WHERE id=?", (new_name, new_age, user_id))
        connection.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
    else:
        messagebox.showerror("Error", "Please enter the ID of the user to update.")

# Function to delete data from the database
def delete_data():
    user_id = id_entry.get()

    if user_id:
        cursor.execute("DELETE FROM people WHERE id=?", (user_id,))
        connection.commit()
        messagebox.showinfo("Success", "Data deleted successfully!")
    else:
        messagebox.showerror("Error", "Please enter the ID of the user to delete.")

# Create labels and entry widgets for user input
name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = tk.Label(app, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5)

age_entry = tk.Entry(app)
age_entry.grid(row=1, column=1, padx=5, pady=5)

id_label = tk.Label(app, text="User ID:")
id_label.grid(row=2, column=0, padx=5, pady=5)

id_entry = tk.Entry(app)
id_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons for CRUD operations
insert_button = tk.Button(app, text="Insert", command=insert_data)
insert_button.grid(row=3, column=0, padx=5, pady=5)

fetch_button = tk.Button(app, text="Fetch", command=fetch_data)
fetch_button.grid(row=3, column=1, padx=5, pady=5)

update_button = tk.Button(app, text="Update", command=update_data)
update_button.grid(row=4, column=0, padx=5, pady=5)

delete_button = tk.Button(app, text="Delete", command=delete_data)
delete_button.grid(row=4, column=1, padx=5, pady=5)

# clear_button = tk.Button(app, text="Clear Table", command=clear_table)
# clear_button.grid(row=5, column=0, padx=5, pady=5)

# Call create_table to ensure the database and table exist
create_table()

# Function to close the application
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        connection.close()
        app.destroy()

# Run the application
app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()