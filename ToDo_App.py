import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Todo App')
root.geometry('400x540')
root.resizable(False, False)

task_list = []

def open_tasks():
    try:
        with open('tasklist.txt', 'r') as file:
            tasks = file.readlines()
        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        open('tasklist.txt', 'w').close()

def add_task(event):
    task = task_entry.get().strip()
    task_entry.delete(0, tk.END)
    if task and task not in task_list:
        with open('tasklist.txt', 'a') as file:
            file.write(f'{task}\n')
        task_list.append(task)
        listbox.insert(tk.END, task)

def delete_task():
    task = str(listbox.get(tk.ANCHOR)).strip()
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'w') as file:
            for t in task_list:
                file.write(f'{t}\n')
        listbox.delete(tk.ANCHOR)
        listbox.selection_clear(0, tk.END)

heading = ttk.Label(root, text='ALL TASKS', font='arial 20 bold')
heading.pack(pady=10)

frame = ttk.Frame(root, width=400, height=50)
frame.pack(pady=20)

task_entry = ttk.Entry(frame, font='arial 18', width=27)
task_entry.pack()
task_entry.focus()
task_entry.bind("<Return>", add_task)

frame1 = ttk.Frame(root, width=300, height=280)
frame1.pack()

listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16)
listbox.pack(side='left', padx=2)

scrollbar = ttk.Scrollbar(frame1)
scrollbar.pack(side='right', fill='y')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_tasks()

s = ttk.Style()
s.configure('TButton', font=('arial', 12))

delete_btn = ttk.Button(root, text="Delete", command=delete_task, style='TButton')
delete_btn.pack(side='bottom', pady=12, ipadx=10, ipady=15)

root.mainloop()