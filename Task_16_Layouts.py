import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Layouts")
root.geometry('500x400')

hello_label = ttk.Label(root, text="Hello, World!", background="orange")
welcome_label = ttk.Label(root, text="Welcome", background="Yellow")

#hello_label.pack(side=tk.TOP, fill=tk.X)
#welcome_label.pack(side=tk.BOTTOM, fill=tk.X)

root.columnconfigure(0)
root.columnconfigure(1)
root.columnconfigure(2)
root.rowconfigure(0)
root.rowconfigure(1)

hello_label.grid(row=0, column=0, columnspan=3, sticky='ew')
welcome_label.grid(row=1, column=0, columnspan=3, sticky='ew')

root.mainloop()