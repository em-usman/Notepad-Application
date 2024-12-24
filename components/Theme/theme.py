import os
from PIL import Image, ImageTk
import tkinter as tk

# Function to calculate the correct path for icons
def get_icons_dir():
    # Get the current file's directory (i.e., components/Theme)
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Navigate one level up and then go to Theme/color
    icons_dir = os.path.join(base_path, 'color')
    return icons_dir


# Function to safely load and resize icons
def load_icon(filename, scale_factor=2):
    icons_dir = get_icons_dir()  # Get the correct icons directory path
    icon_path = os.path.join(icons_dir, filename)
    print(f"Loading icon from: {icon_path}")  # Debug: print the path
    if not os.path.exists(icon_path):
        raise FileNotFoundError(f"Icon not found: {icon_path}")
    
    # Open and resize the image
    image = Image.open(icon_path)
    image = image.resize((32, 32), Image.Resampling.LANCZOS)  # Resize image to 32x32
    return ImageTk.PhotoImage(image)


# Function to change the theme
def change_theme(text_editor, bg_color, fg_color):
    # Change the background and foreground colors of the text editor
    text_editor.config(bg=bg_color, fg=fg_color)


# Main Theme function to create the color theme menu and labels
def Theme(menu, text_editor):
    # Load the icons using the correct path
    black_icon = load_icon("black.png")
    white_icon = load_icon("white.png")
    pink_icon = load_icon("pink.png")
    skyblue_icon = load_icon("skyblue.png")
    cream_icon = load_icon("cream.png")

    # Create the color theme menu
    color_theme = tk.Menu(menu, tearoff=False)

    # Map theme colors to the menu items
    color_icon = [black_icon, white_icon, pink_icon, skyblue_icon, cream_icon]
    color_dict = {
        "black": ('#0c0d0c', "#fcfcfc"),
        "white": ('#fcfcfc', '#0c0d0c'),
        "pink": ('#ffccf4', '#0c0d0c'),
        "skyblue": ('#91d3ff', '#0c0d0c'),
        "cream": ('#f5f7e6', '#0c0d0c')
    }

    # Store references to the icons to prevent them from being garbage collected
    icon_references = []  # Store references for the icons

    # Add labels and radiobuttons for each theme to the menu
    count = 0
    for theme, colors in color_dict.items():
        icon_references.append(color_icon[count])  # Keep a reference to each icon
        color_theme.add_radiobutton(
            label=theme.capitalize(),
            image=color_icon[count],  # Assign the image to the menu item
            compound=tk.LEFT,
            command=lambda bg=colors[0], fg=colors[1]: change_theme(text_editor, bg, fg)
        )
        count += 1

    # Option to reset to default theme (optional)
    color_theme.add_separator()
    color_theme.add_command(
        label="Default Theme",
        command=lambda: change_theme(text_editor, "#fcfcfc", "#0c0d0c")  # Example default colors
    )

    # Add the color theme menu as a dropdown to the main menu
    menu.add_cascade(label="Theme", menu=color_theme)

    # Return the menu so it can be used elsewhere if needed
    return color_theme
