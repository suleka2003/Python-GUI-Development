import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Frames")
root.geometry("400x300")

frame1 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack(side="bottom")

entry = ttk.Entry(frame1)
entry.pack(pady=10)

button = ttk.Button(frame1, text="Submit")
button.pack()

frame2 = ttk.Frame(root, width=200, height=500, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side="right")

lable1 = ttk.Label(frame2, text="Welcome")
lable1.pack()

button2 = ttk.Button(frame2, text="Click Me")
button2.pack(pady=20)

root.mainloop()