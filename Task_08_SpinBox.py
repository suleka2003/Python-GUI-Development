import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()
root.title("Spin Box")
root.geometry('300x200')
root.resizable(False, False)

# Get month names (skip the first empty string)
months = list(month_name)[1:]

spin_var = tk.StringVar()

def select_spin():
    label.configure(text="Selected: " + spin_var.get())

spin = ttk.Spinbox(root, values=months, textvariable=spin_var, command=select_spin)
spin.pack()

label = ttk.Label(root, text='Select a month:')
label.pack()

root.mainloop()