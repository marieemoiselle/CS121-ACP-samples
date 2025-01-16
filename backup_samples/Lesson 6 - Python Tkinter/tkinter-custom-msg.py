import tkinter as tk

def show_info():
    # define the message to display
    message = "Keep slayin'!"
    # create a Message widget with the specified properties
    info_message = tk.Message(root, text=message, width=300, font=("Arial", 14), bg="pink", fg="black")
    # pack the Message widget into the window
    info_message.pack()

# create the main application window
root = tk.Tk()
root.title("Display Message on Click")

# create a button to trigger the show_info function
info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack()

# start the Tkinter event loop
root.mainloop()
