import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()
root.title("Combo Box")
root.geometry('300x200')
root.resizable(False, False)

combo_var = tk.StringVar()

def select_combo(event):
    label.configure(text="Selected: " + combo_var.get())

combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = month_name[1:]
combo.bind('<<ComboboxSelected>>', select_combo)
combo.pack()

label = ttk.Label(root, text='Select a month:')
label.pack()

root.mainloop()