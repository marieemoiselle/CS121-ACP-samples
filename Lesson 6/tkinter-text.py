import tkinter as tk

def show_text():
    entered_text = text_widget.get("1.0", tk.END)
    print("Entered text:", entered_text)

root = tk.Tk()
root.title("Text Widget In Tkinter")

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

text_button = tk.Button(root, text="Show Text", command=show_text)
text_button.pack()

root.mainloop()