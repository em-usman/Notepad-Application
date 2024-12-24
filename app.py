import tkinter as tk
from components.View.view import View
from components.File.file import File
from components.Edit.edit import Edit
from components.Toolbar.toolbar import toolbar
from components.Theme.theme import Theme

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

# App icon set:
# root.wm_iconbitmap('mainicon.ico')

# Create the main text area:
text_area = tk.Text(root, wrap="word", undo=True, font=("Arial", 12))

# Initialize the main menu:
menu = tk.Menu(root)
root.config(menu=menu)  # Link the menu to the root window

# Show toolbar by default (using the toolbar function)
toolbar_frame = toolbar(root, text_area)
toolbar_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)  # Toolbar is packed first

# Add File Menu:
fileMenu = File(root, text_area)
menu.add_cascade(label="File", menu=fileMenu)

# Add View Menu (ensure View menu is working correctly):
viewMenu = View(root, text_area, toolbar_frame)
menu.add_cascade(label="View", menu=viewMenu)

# Add Edit Menu:
editMenu = Edit(root, text_area)
menu.add_cascade(label="Edit", menu=editMenu)


#Add Theme Menu:
themeMenu = Theme(menu, text_area)
# menu.add_cascade(label="Theme", menu=themeMenu)
# Then pack the text area below the toolbar
text_area.pack(expand=1, fill="both")

# End the GUI:
root.mainloop()


