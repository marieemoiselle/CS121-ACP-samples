import tkinter as tk
from tkinter import font

# creating a Tkinter window
root = tk.Tk()
root.title("Custom Fonts in Tkinter")

# creating a font object
custom_font = font.Font(family="Lora", size=12, weight="bold")

# creating a label widget with some text
label = tk.Label(root, text="This label will be slaying later.", font=custom_font, bg="black", fg="pink")
label.pack()

# starting the Tkinter event loop
root.mainloop()