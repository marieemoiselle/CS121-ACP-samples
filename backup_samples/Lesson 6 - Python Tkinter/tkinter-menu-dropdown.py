import tkinter as tk

def on_subitem_click(subitem):
    print(f"Subitem {subitem} clicked!")

root = tk.Tk()
root.title("Tkinter Dropdown Menu")

# create the main menu
menu = tk.Menu(root)

# create a submenu
submenu = tk.Menu(menu)

# add subitems to the submenu
submenu.add_command(label="Cherry", command=lambda: on_subitem_click(1))
submenu.add_command(label="Strawberry", command=lambda: on_subitem_click(2))
submenu.add_command(label="Peach", command=lambda: on_subitem_click(3))
submenu.add_command(label="Lychee", command=lambda: on_subitem_click(4))

# add the submenu to the main menu as a cascade
menu.add_cascade(label="Fruits", menu=submenu)

# configure the root window's menu
root.config(menu=menu)

# initialize main event
root.mainloop()