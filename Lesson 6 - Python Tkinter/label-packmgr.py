import tkinter as tk

# creating a Tkinter window
root = tk.Tk()
root.title("Pack Manager")

# creating label widgets
label1 = tk.Label(root, text="Fatima Marie P. Agdon")
label2 = tk.Label(root, text="@marieemoiselle")

# using pack() to position the labels in a vertical stack
label1.pack()
label2.pack()

# running the Tkinter event loop
root.mainloop()