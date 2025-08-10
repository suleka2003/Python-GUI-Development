import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabs")
root.geometry("500x400")

def add_name():
    name = entry_value.get()
    if name:
        table.insert("", "end", values=(name,))
        entry_value.set("")

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook, width=200, height=100, relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack()

entry_value = tk.StringVar()

entry = ttk.Entry(frame1, textvariable=entry_value)
entry.pack(pady=10)

button = ttk.Button(frame1, text="Submit", command=lambda: add_name())
button.pack()

frame2 = ttk.Frame(notebook, width=200, height=100, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

table = ttk.Treeview(frame2, columns=("Names"), show="headings")
table.column("Names", width=198)
table.heading("Names", text="Names")
table.pack()

names = ["Kamal", "Saman"]
for name in names:
    table.insert("", "end", values=(name,))

notebook.add(frame1, text="input")
notebook.add(frame2, text="output")
notebook.pack()

root.mainloop()