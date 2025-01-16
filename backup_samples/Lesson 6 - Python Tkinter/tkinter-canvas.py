import tkinter as tk

# creating the main application window
root = tk.Tk()
root.title("Tkinter Canvas")

# creating a canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")

# adding the canvas to the window
canvas.pack()

# starting the Tkinter event loop
root.mainloop()