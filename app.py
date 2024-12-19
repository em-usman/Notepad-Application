import tkinter as tk
from tkinter import * 
from components.File.file import File 

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


## ------------ Add your widgets here ------------ ##
File(root)




## ------------ Add your widgets here ------------ ##

# End the GUI:
root.mainloop()

