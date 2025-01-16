import tkinter as tk

def on_button_click(event):
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me")
button.pack()

# binding the button click event to the callback function
button.bind("<Button-1>", on_button_click)

root.mainloop()