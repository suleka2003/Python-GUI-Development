import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Basic widgets")
root.geometry("300x200")
root.resizable(False, False)

def button_click():
    entry_field_value = entry.get()
    label.configure(text=entry_field_value)
    button.configure(state="disabled")
    print(entry_field_value)

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Click Me", command=button_click)
button.pack()

label = ttk.Label(root)
label.pack()

root.mainloop()