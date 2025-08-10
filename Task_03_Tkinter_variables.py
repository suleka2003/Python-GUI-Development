import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Variables")
root.geometry("300x200")

variable_value = tk.StringVar(value="Welcome") # default value

label = ttk.Label(root, textvariable=variable_value)
label.pack()

entry = ttk.Entry(root, textvariable=variable_value)
entry.pack()

button = ttk.Button(root, text="Click me", command=lambda:print(entry.get()))
button.pack()

root.mainloop()