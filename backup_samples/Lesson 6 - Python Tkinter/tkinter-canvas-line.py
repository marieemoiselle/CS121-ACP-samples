import tkinter as tk

# creating Tkinter window
root = tk.Tk()
root.title("Drawing Lines on Canvas")

# creating canvas widget
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# drawing a line on the canvas from (50, 50) to (200, 100)
canvas.create_line(50, 50, 200, 100, fill="#FF007F", width=2)

# starting the Tkinter event loop
root.mainloop()