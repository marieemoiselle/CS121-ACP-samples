import tkinter as tk

# creating the main application window
root = tk.Tk()

# creating a label
label = tk.Label(root, text="Bonjour, Mademoiselle Marie!")

# placing the label in the window
label.pack()

# starting the Tkinter event loop
root.mainloop()