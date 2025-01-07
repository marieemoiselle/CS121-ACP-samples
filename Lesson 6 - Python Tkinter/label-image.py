import tkinter as tk

# creating a Tkinter window
root = tk.Tk()
root.title("Displaying Images")

# creating a PhotoImage object with the image file path
image = tk.PhotoImage(file="squad.png")

# creating a label widget to display the image
label = tk.Label(root, image=image)
label.pack()

# running the Tkinter event loop
root.mainloop()