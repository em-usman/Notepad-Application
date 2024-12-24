import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function to resize images
def resize_image(image_path, size=(32, 32)):
    image = Image.open(image_path)
    image = image.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsizing
    return ImageTk.PhotoImage(image)

# Function to change the theme
def change_theme(bg_color, fg_color):
    text_editor.config(bg=bg_color, fg=fg_color)

# Create main application window
main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Notepad")
# Create main menu
main_menu = tk.Menu()

#------------------COLOR THEME--------------------------
black_icon = resize_image("F:/Notepad app/Notepad-Application/components/Theme/color/black.png")
white_icon = resize_image("F:/Notepad app/Notepad-Application/components/Theme/color/white.png")
pink_icon = resize_image("F:/Notepad app/Notepad-Application/components/Theme/color/pink.png")
skyblue_icon = resize_image("F:/Notepad app/Notepad-Application/components/Theme/color/skyblue.png")
cream_icon = resize_image("F:/Notepad app/Notepad-Application/components/Theme/color/cream.png")

color_theme = tk.Menu(main_menu, tearoff=False)

# Color theme set
color_icon = (black_icon, white_icon, pink_icon, skyblue_icon, cream_icon)

color_dict = {
    "black": ('#0c0d0c', "#fcfcfc"),
    "white": ('#fcfcfc', '#0c0d0c'),
    "pink": ('#ffccf4', '#0c0d0c'),
    "skyblue": ('#91d3ff', '#0c0d0c'),
    "cream": ('#f5f7e6', '#0c0d0c')
}

count = 0 
for theme, colors in color_dict.items():
    color_theme.add_radiobutton(label=theme, image=color_icon[count], compound=tk.LEFT, command=lambda bg=colors[0], fg=colors[1]: change_theme(bg, fg))
    count += 1

# Create a Text widget for the text editor
text_editor = tk.Text(main_application, wrap='word', relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH, expand=True)

# Configure the scrollbar for the text editor
scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_editor.yview)

#---------------MENU CASCADE--------------------
main_menu.add_cascade(label="Color Theme", menu=color_theme)

main_application.config(menu=main_menu)
main_application.mainloop()
