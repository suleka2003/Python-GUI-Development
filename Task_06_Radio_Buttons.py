import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Radio Buttons")
root.geometry('300x200')
root.resizable(False, False)

radio_var = tk.StringVar()

def select_radio():
    label.configure(text="Selected: " + radio_var.get())

radio1 = ttk.Radiobutton(root, text='Python', variable=radio_var, value='Python', command=select_radio)
radio1.pack()

radio2 = ttk.Radiobutton(root, text='Java', variable=radio_var, value='Java', command=select_radio)
radio2.pack()

radio3 = ttk.Radiobutton(root, text='C++', variable=radio_var, value='C++', command=select_radio)
radio3.pack()

label = ttk.Label(root, text='Select a programming language:')
label.pack()

root.mainloop()