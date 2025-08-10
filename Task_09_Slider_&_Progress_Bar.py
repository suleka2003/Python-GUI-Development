import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Slider & Progress Bar")
root.geometry('300x200')
root.resizable(False, False)

scale_value = tk.DoubleVar(value=50)

value_label = ttk.Label(root, text=f"{scale_value.get():.2f}")
value_label.pack()

def update_value_label(value):
    value_label.config(text=f"{float(value):.2f}")

scale = ttk.Scale(root, command=update_value_label, from_=0, to=100, variable=scale_value)
scale.pack()

progress_bar = ttk.Progressbar(root, variable=scale_value)
progress_bar.pack()

root.mainloop()