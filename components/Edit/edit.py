import tkinter as tk
from tkinter import Menu, messagebox
import os

def Edit(root, text_editor):
    # Base path calculation for the icons
    base_path = os.path.dirname(os.path.abspath(__file__))
    icons_dir = os.path.abspath(os.path.join(base_path, '../../icons2'))

    # Function to safely load and resize icons
    def load_icon(filename, scale_factor=2):
        icon_path = os.path.join(icons_dir, filename)
        if not os.path.exists(icon_path):
            raise FileNotFoundError(f"Icon not found: {icon_path}")
        icon = tk.PhotoImage(file=icon_path)
        return icon.subsample(scale_factor, scale_factor)  # Resize icon

    # Edit icons
    try:
        copy_icon = load_icon('copy.png')
        paste_icon = load_icon('paste.png')
        cut_icon = load_icon('cut.png')
        clear_icon = load_icon('clear.png')
        find_icon = load_icon('find.png')
    except FileNotFoundError as e:
        print(e)
        messagebox.showerror("Icon Error", f"An error occurred while loading icons:\n{e}")
        return

    # Keep a reference to the icons for Tkinter menu
    root.copy_icon = copy_icon
    root.paste_icon = paste_icon
    root.cut_icon = cut_icon
    root.clear_icon = clear_icon
    root.find_icon = find_icon

    # Function to copy selected text
    def copy_text(event=None):
        text_editor.event_generate("<<Copy>>")

    # Function to paste text from the clipboard
    def paste_text(event=None):
        text_editor.event_generate("<<Paste>>")

    # Function to cut selected text
    def cut_text(event=None):
        text_editor.event_generate("<<Cut>>")

    # Function to clear all text
    def clear_all(event=None):
        text_editor.delete(1.0, tk.END)

    # Function to find text
    def find_text(event=None):
        find_dialog = tk.Toplevel()
        find_dialog.title("Find Text")
        find_dialog.geometry("400x200")

        find_label = tk.Label(find_dialog, text="Find: ")
        find_label.pack(pady=10)

        find_entry = tk.Entry(find_dialog, width=30)
        find_entry.pack(pady=10)

        def find():
            text_editor.tag_remove("match", "1.0", tk.END)
            start_pos = "1.0"
            query = find_entry.get()
            if query:
                while True:
                    start_pos = text_editor.search(query, start_pos, stopindex=tk.END)
                    if not start_pos:
                        break
                    end_pos = f"{start_pos}+{len(query)}c"
                    text_editor.tag_add("match", start_pos, end_pos)
                    start_pos = end_pos
                    text_editor.tag_config("match", foreground="red", background="yellow")

        find_button = tk.Button(find_dialog, text="Find", command=find)
        find_button.pack(pady=10)

        close_button = tk.Button(find_dialog, text="Close", command=find_dialog.destroy)
        close_button.pack(pady=10)

    # Create the Edit menu (ensure it is a correct menu object)
    edit_menu = Menu(root, tearoff=0)

    # Add commands with resized icons
    edit_menu.add_command(
        label='Copy',
        image=root.copy_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+C',
        command=copy_text
    )
    edit_menu.add_command(
        label='Paste',
        image=root.paste_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+V',
        command=paste_text
    )
    edit_menu.add_command(
        label='Cut',
        image=root.cut_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+X',
        command=cut_text
    )
    edit_menu.add_command(
        label='Clear All',
        image=root.clear_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+Shift+C',
        command=clear_all
    )
    edit_menu.add_command(
        label='Find',
        image=root.find_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+F',
        command=find_text
    )

    # Bind shortcut keys
    root.bind("<Control-c>", copy_text)
    root.bind("<Control-v>", paste_text)
    root.bind("<Control-x>", cut_text)
    root.bind("<Control-Shift-c>", clear_all)
    root.bind("<Control-f>", find_text)

    return edit_menu


