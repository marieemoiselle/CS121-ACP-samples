# importing the tkinter library
import tkinter as tk

# creating the main application window
root = tk.Tk()
root.title("Tkinter Button")

# creating a button
button = tk.Button(root, text="Click the button")

# placing the button in the window
button.pack()

# running the Tkinter event loop
root.mainloop()