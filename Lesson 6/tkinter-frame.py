import tkinter as tk

root = tk.Tk()
root.title("Frames in Tkinter")

# Create the outer frame with a pink background
outer_frame = tk.Frame(root, bg="pink", bd=10)  
# Adding a border for visibility

# Create the inner frame with a light blue background, nested inside the outer frame
inner_frame = tk.Frame(outer_frame, bg="lightblue", bd=5)  
# Adding a border for visibility

# Create labels for each frame
label1 = tk.Label(inner_frame, text="Label inside inner frame", bg="lightblue")
label2 = tk.Label(outer_frame, text="Label inside outer frame", bg="pink")

# Pack the labels inside their respective frames
label1.pack(padx=10, pady=10)  
# Adding padding to make the inner frame's color visible

label2.pack(padx=10, pady=10)  
# Adding padding to make the outer frame's color visible

# Pack the inner frame inside the outer frame
inner_frame.pack(padx=10, pady=10)  # Adding padding around the inner frame

# Pack the outer frame in the window
outer_frame.pack(padx=20, pady=20)  # Adding padding around the outer frame

# Initialize the main event loop
root.mainloop()
