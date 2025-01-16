import tkinter as tk

root = tk.Tk()
root.title("Checkbuttons in Tkinter")

# creating additional Boolean variables
option1_var = tk.BooleanVar()
option2_var = tk.BooleanVar()

def on_option1_click():
    if option1_var.get():
        print("Option 1 has been selected!")
    else:
        print("Option 1 has been deselected!")

def on_option2_click():
    if option2_var.get():
        print("Option 2 has been selected!")
    else:
        print("Option 2 has been deselected!")

# creating multiple checkbuttons
checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=option1_var, command=on_option1_click)
checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=option2_var, command=on_option2_click)

# placing the checkbuttons in the window
checkbutton1.pack()
checkbutton2.pack()

root.mainloop()