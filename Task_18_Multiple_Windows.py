import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

value = tk.IntVar(value=0)

def increment_value():
    value.set(value.get() + 1)

def create_sub_window():
    global sub_window
    sub_window = tk.Toplevel()
    sub_window.title("Sub Window")
    sub_window.geometry("300x200")
    sub_button = ttk.Button(sub_window, text="Click Me", command=increment_value)
    sub_button.pack()
    sub_label = ttk.Label(sub_window, textvariable=value)
    sub_label.pack()

def close_sub_window():
    sub_window.destroy()

main_button = ttk.Button(root, text="Open sub window", command=create_sub_window)
main_button.pack()

close_sub_button = ttk.Button(root, text="Close sub window", command=close_sub_window)
close_sub_button.pack()

root.mainloop()