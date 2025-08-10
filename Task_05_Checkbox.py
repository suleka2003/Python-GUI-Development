import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Checkbox")
root.geometry('300x200')
root.resizable(False, False)

label_var = tk.StringVar()
check1_var = tk.BooleanVar()
check2_var = tk.BooleanVar()

def checkbox_results():
    selected = []
    if check1_var.get():
        selected.append("Python")
    if check2_var.get():
        selected.append("Java")
    output_string = "Selected Languages: " + ", ".join(selected) if selected else "No language selected"
    label_var.set(output_string)

check1 = ttk.Checkbutton(root, text="Python", variable=check1_var)
check1.pack()

check2 = ttk.Checkbutton(root, text="Java", variable=check2_var)
check2.pack()

button = ttk.Button(root, text="Show Selected", command=checkbox_results)
button.pack()

label = ttk.Label(root, textvariable=label_var)
label.pack()

root.mainloop()