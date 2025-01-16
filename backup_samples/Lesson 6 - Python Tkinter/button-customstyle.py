import tkinter as tk
from tkinter import ttk

def on_button_click():
     print("Button clicked!")

# creating the root window
root = tk.Tk()
root.title("Custom Button Styling")

# creating a ttk button
button = ttk.Button(root, text="Custom-Styled Button", command=on_button_click)

# creating a custom style for the button
style = ttk.Style()
style.configure("Custom.TButton", relief=tk.RAISED, borderwidth=5, padx=10, pady=5, font=("Courier New", 12, "bold"))

# applying the custom style to the button
button.configure(style="Custom.TButton")

# packing the button
button.pack(pady=20)

# running the Tkinter main loop
root.mainloop()