import tkinter as tk

# function to handle item selection in the listbox
def on_selection(event):
    selected_indices = listbox.curselection()
    for index in selected_indices:
        item = listbox.get(index)
        print("Selected:", item)

# function to delete the selected item in the listbox
def delete_selected_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        index_to_delete = selected_indices[0]
        listbox.delete(index_to_delete)

# function to select the first item in the listbox
def select_first_item():
    if listbox.size() > 0:  # Check if there are items in the listbox
        listbox.select_set(0)  # Select the first item
        listbox.event_generate("<<ListboxSelect>>")  # Trigger selection event

# create the main window
root = tk.Tk()
root.title("ListBox in Tkinter")

# create the listbox widget
listbox = tk.Listbox(root)
listbox.pack()

# populate the listbox with items
listbox.insert(tk.END, "Peach")
listbox.insert(tk.END, "Cherry")
listbox.insert(tk.END, "Strawberry")
listbox.insert(tk.END, "Lychee")
listbox.insert(tk.END, "Raspberry")

# bind the on_selection function to the <<ListboxSelect>> event
listbox.bind("<<ListboxSelect>>", on_selection)

# create a button to delete the selected item
delete_button = tk.Button(root, text="Delete Selected Item", command=delete_selected_item)
delete_button.pack()

# create a button to select the first item
select_button = tk.Button(root, text="Select First Item", command=select_first_item)
select_button.pack()

# start the main event loop
root.mainloop()
