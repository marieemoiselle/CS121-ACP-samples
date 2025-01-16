import tkinter as tk
from tkinter import font

# Function to change the button text
def change_text():
    button.config(text="The button was clicked.")

# creating a Tkinter window
root = tk.Tk()
root.title("Changing Button Colors")

# creating a font object
custom_font = font.Font(family="Gill Sans MT", size=14, weight="bold")

# creating a button widget and place it on the window
button = tk.Button(root, text="Click the button", font=custom_font, command=change_text)
button.pack()

# setting the background and foreground colors for the button
button.config(bg="pink", fg="black")

# running the Tkinter event loop
root.mainloop()