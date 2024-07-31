import tkinter as tk

def on_menu_item_click():
    print("Menu item clicked!")

root = tk.Tk()
root.title("Menu Example")

# create a menu
menu = tk.Menu(root)

# add menu items to the menu
menu.add_command(label="Option 1", command=on_menu_item_click)
menu.add_separator()
menu.add_command(label="Option 2", command=on_menu_item_click)
menu.add_separator()
menu.add_command(label="Option 3", command=on_menu_item_click)
menu.add_separator()
menu.add_command(label="Option 4", command=on_menu_item_click)

# configure the root window's menu
root.config(menu=menu)

root.mainloop()