import tkinter as tk

# creating a Tkinter window
root = tk.Tk()
root.title("Using Place Manager")

# creating a label widget
label = tk.Label(root, text="Bonjour, Mademoiselle Marie!")

# using place() to position the label with x and y coordinates
label.place(x=50, y=100)

# starting the Tkinter event loop
root.mainloop()