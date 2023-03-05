from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Application")

# Use a consistent color scheme
root.configure(bg="#333")

# Use fonts effectively
label = Label(root, text="Hello, World!", font=("Helvetica", 24), fg="#333")
label.pack(pady=20)

# Use padding and spacing
button = ttk.Button(root, text="Click me!", padding=10)
button.pack(pady=10)

# Use frames and borders
frame = ttk.Frame(root, relief="solid", borderwidth=1)
label = Label(frame, text="This is a frame")
label.pack(pady=10)
frame.pack(pady=10)

# Use styles
style = ttk.Style()
style.configure("My.TButton", background="#333", foreground="#fff", font=("Helvetica", 14))
button = ttk.Button(root, text="Styled Button", style="My.TButton")
button.pack(pady=10)

# Use layouts effectively
label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

root.mainloop()