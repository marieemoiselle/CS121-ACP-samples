import tkinter as tk

# creating the main window
root = tk.Tk()
root.title("Tkinter Entry Widget")

def on_button_click():
    name_input = name_entry.get()
    age_input = age_entry.get()
    
    print(f"User name: {name_input}")
    print(f"Age: {age_input}")

def validate_input(value):
    return value.isdigit() or value == ""  
    # allow only numeric input and empty string

# creating an entry widget for the name
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
name_entry.insert(0, "Enter your name")  # Set a default value

# creating an entry widget for the age with validation
age_label = tk.Label(root, text="Enter your age:")
age_label.pack()
validate_age = root.register(validate_input)  # Register the validation function
age_entry = tk.Entry(root, validate="key", validatecommand=(validate_age, '%P'))
age_entry.pack()

# creating a button widget
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

# initialize the main event loop
root.mainloop()
