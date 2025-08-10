import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Buttons")
root.geometry('300x200')

def button_func(num1, num2):
    sum = num1 + num2
    ans.set(f"Answer is {sum}")

num1 = tk.IntVar()
num2 = tk.IntVar()
ans = tk.StringVar()

entry1 = ttk.Entry(root, textvariable = num1)
entry1.pack()
entry2 = ttk.Entry(root, textvariable = num2)
entry2.pack()

button = ttk.Button(root, text = "Click me", command = lambda: button_func(num1.get(), num2.get()))
button.pack()

label = ttk.Label(root, textvariable = ans)
label.pack()

root.mainloop()