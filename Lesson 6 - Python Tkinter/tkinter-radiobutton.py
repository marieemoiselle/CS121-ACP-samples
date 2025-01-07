import tkinter as tk

# create the main application window
root = tk.Tk()
root.title("Tkinter Radio Buttons")

# define the variable to hold the value of the selected radio button
option_var = tk.IntVar()

# create radio buttons and associate them with the variable
radiobutton1 = tk.Radiobutton(root, text="Cherry", variable=option_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Peach", variable=option_var, value=2)
radiobutton3 = tk.Radiobutton(root, text="Strawberry", variable=option_var, value=3)
radiobutton4 = tk.Radiobutton(root, text="Lychee", variable=option_var, value=4)

# pack the radio buttons into the window
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

# start the Tkinter event loop
root.mainloop()
