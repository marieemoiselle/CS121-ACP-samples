import tkinter as tk

# creating a Tkinter window
root = tk.Tk()
root.title("Labels in Grid Manager")

# creating label widgets
label1 = tk.Label(root, text="Fatima")
label2 = tk.Label(root, text="Marie")

# using grid() to position the labels in rows and columns
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

# starting the Tkinter event loop
root.mainloop()