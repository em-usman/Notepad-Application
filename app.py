import tkinter as tk
from tkinter import Menu
from components.File.file import File
from components.View.view import View

# Start the GUI:
root = tk.Tk()

# Set the window size and center the application on the screen:
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Center the window with a medium size:
center_window(root, 800, 600)

# Set window title:
root.title("Notepad Application")

# Create the main text area:
text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", 12))
text_area.pack(expand=1, fill="both")

# Initialize the main menu:
menu = Menu(root)
root.config(menu=menu)

# Add File Menu:
fileMenu = File(root, text_area)
menu.add_cascade(label="File", menu=fileMenu)

# Add View Menu:
viewMenu = View(root, text_area)
menu.add_cascade(label="View", menu=viewMenu)

# End the GUI:
root.mainloop()
