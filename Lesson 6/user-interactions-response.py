import tkinter as tk

def on_key_press(event):
    print(f"Key '{event.char}' was pressed!")

def on_mouse_move(event):
    print(f"Mouse moved to ({event.x}, {event.y})")
    
root = tk.Tk()
root.bind("<Key>", on_key_press)
root.bind("<Motion>", on_mouse_move)
root.mainloop()