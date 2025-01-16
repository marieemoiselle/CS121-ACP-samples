import tkinter as tk
# create the main application window
root = tk.Tk()
root.title("Messages in Tkinter")

# create a Message widget
message = tk.Message(root, text="This message widget has many lines.\nMultiple lines of text are supported.\nAnd here's another one.")

# place the Message widget in the window
message.pack()

# start the Tkinter event loop
root.mainloop()