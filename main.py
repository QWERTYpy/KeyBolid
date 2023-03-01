from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

enabled = IntVar()

enabled_checkbutton = ttk.Checkbutton(root, variable=enabled)
enabled_checkbutton.place(x=0, y=0)
print(enabled.get())
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.place(x=40,y=40)

root.mainloop()