import tkinter as tk
from tkinter import ttk

# creating the root window
root = tk.Tk()
root.title("Additional Styling")

styled_button = ttk.Button(root, text="Styled Button", style="Custom.TButton")
styled_button.pack()

# adding custom styles
style = ttk.Style()
style.configure("Custom.TButton", foreground="#FC8EAC", font=("Poppins", 14))

# starting the Tkinter main loop
root.mainloop()