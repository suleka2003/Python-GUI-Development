import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Message boxes")
root.geometry("500x400")

def open_message_box():
    result = messagebox.showinfo("Information", "This is an info message.")
    if result == "ok":
        print("User clicked OK")
    result = messagebox.showerror("Error", "An error has occurred!")
    if result == "ok":
        print("User clicked OK")
    result = messagebox.showwarning("Warning", "This is a warning message.")
    if result == "ok":
        print("User clicked OK")
    result = messagebox.askyesno("Confirmation", "Do you want to proceed?")
    if result:
        print("User chose Yes")
    result = messagebox.askretrycancel("Retry", "Do you want to retry?")
    if result:
        print("User chose to retry")

button = ttk.Button(root, text="Click Me", command=open_message_box)
button.pack(pady=20)

root.mainloop()