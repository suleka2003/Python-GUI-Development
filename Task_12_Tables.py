import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tree view")
root.geometry("450x400")

table = ttk.Treeview(root, columns=("Name", "Age", "City"), show='headings')
table.pack(fill="both", expand=True)

table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("City", text="City")
table.column("Age", width=50, anchor='center')

name = ["Alice", "Bob", "Charlie", "David"]
age = [30, 25, 35, 40]
city = ["New York", "Los Angeles", "Chicago", "Houston"]

def selected_item(event):
    print(table.item(table.selection())['values'])

for i in range(len(name)):
    table.insert("", i, values=(name[i], age[i], city[i]))

table.bind("<<TreeviewSelect>>", lambda event: selected_item(event))

root.mainloop()