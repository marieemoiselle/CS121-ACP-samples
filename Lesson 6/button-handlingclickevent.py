import tkinter as tk

# function for the button click
def on_button_click():
    print("Button clicked!")

# creating Tkinter window
root = tk.Tk()
root.title("Handling Button Click Events")

# creating button widget and bind the function to its click event
button = tk.Button(root, text="Click the button", command=on_button_click)
button.pack()

# start the Tkinter event loop
root.mainloop()