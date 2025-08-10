import tkinter as tk

# create a window
root = tk.Tk()

width, height = 500, 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
left = screen_width // 2 - width // 2
top = screen_height // 2 - height // 2

# provide width and height of the window
root.geometry(f"{width}x{height}+{left}+{top}")

# give a title
root.title("Hello world")

# make them unresizable
root.resizable(False, False)

# run the window
root.mainloop()

print("Code ran successfully")