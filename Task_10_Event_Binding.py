import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Events")
root.geometry("300x200")
root.resizable(False, False)

button = ttk.Button(root, text="Click Me")
button.pack()

root.bind("<Key>", lambda event: print(f"Key pressed: {event.char}"))

root.mainloop()