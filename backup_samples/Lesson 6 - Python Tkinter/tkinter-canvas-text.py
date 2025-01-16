import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Drawing Text on Canvas")

# Create a canvas widget with a width and height of 400 pixels
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw text on the canvas
# (200, 200) specifies the coordinates for the center of the text
# text="This is a text drawn in Tkinter!" specifies the text to display
# font=("Permanent Marker", 16) sets the font to "Permanent Marker" with a size of 16
# fill="#FF007F" sets the text color to a specific shade of pink
canvas.create_text(200, 200, text="This is a text drawn in Tkinter!", font=("Permanent Marker", 16), fill="#FF007F")

# Start the Tkinter event loop to display the window
root.mainloop()
