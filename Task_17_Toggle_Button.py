import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Toggle Button")
root.geometry('300x200')

def change_state():
    if bulb['text'] == "OFF":
        bulb['text'] = "ON"
    else:
        bulb['text'] = "OFF"

switch = ttk.Button(root, text="Switch", command=change_state)
switch.pack(side="bottom", pady=20)

bulb = ttk.Label(root, text="OFF")
bulb.place(relx=0.5, rely=0.4, anchor="center")

root.mainloop()