import tkinter as tk

root = tk.Tk()
root.title("Canvas")
root.geometry("500x400")
root.resizable(False, False)

canvas = tk.Canvas(root, bg="white")
canvas.pack()

def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval((x, y, x+5, y+5), fill="black")

canvas.bind("<B1-Motion>", draw)

canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")
canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")
canvas.create_line(50, 200, 450, 200, fill="green", width=3)

root.mainloop()