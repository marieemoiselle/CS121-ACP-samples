import tkinter as tk

# Creating a Tkinter window
root = tk.Tk()
root.title("Drawing Shapes")

# Creating a canvas widget with a width and height of 400 pixels
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Drawing a candy pink rectangle on the canvas
# (100, 150) is the top-left corner of the rectangle
# (250, 250) is the bottom-right corner of the rectangle
canvas.create_rectangle(100, 150, 250, 250, fill="#E4717A")

# Drawing a salmon pink oval on the canvas
# (300, 50) is the top-left corner of the bounding box for the oval
# (350, 100) is the bottom-right corner of the bounding box for the oval
canvas.create_oval(300, 50, 350, 100, fill="#FF91A4")

# Drawing a blush pink polygon on the canvas
# (50, 200), (150, 250), and (100, 300) are the vertices of the polygon
canvas.create_polygon(50, 200, 150, 250, 100, 300, fill="#FFC0CB")

# Initialize the Tkinter event loop to display the window
root.mainloop()
