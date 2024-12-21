import tkinter as tk
from tkinter import Menu, messagebox
import os
import subprocess

def View(root, text_area):
    global font_size, status_bar, word_wrap
    font_size = 12
    word_wrap = True

    # Base path calculation for the icons
    base_path = os.path.dirname(os.path.abspath(_file_))
    icons_dir = os.path.abspath(os.path.join(base_path, '../../icons2'))

    # Function to safely load and resize icons
    def load_icon(filename, scale_factor=2):
        icon_path = os.path.join(icons_dir, filename)
        if not os.path.exists(icon_path):
            raise FileNotFoundError(f"Icon not found: {icon_path}")
        icon = tk.PhotoImage(file=icon_path)
        return icon.subsample(scale_factor, scale_factor)  # Resize icon

    # Load icons
    try:
        zoom_in_icon = load_icon('zoom_in.png')
        zoom_out_icon = load_icon('zoom_out.png')
        run_icon = load_icon('run.png')
        status_bar_icon = load_icon('status_bar.png')
        word_wrap_icon = load_icon('word_wrap.png')
    except FileNotFoundError as e:
        print(e)
        messagebox.showerror("Icon Error", f"An error occurred while loading icons:\n{e}")
        return

    # Keep a reference to the icons for Tkinter menu
    root.zoom_in_icon = zoom_in_icon
    root.zoom_out_icon = zoom_out_icon
    root.run_icon = run_icon
    root.status_bar_icon = status_bar_icon
    root.word_wrap_icon = word_wrap_icon

    # Define status bar:
    status_bar = tk.Label(root, text="Line 1, Column 1", anchor="e")
    status_bar.pack(side="bottom", fill="x")

    def update_status_bar(event=None):
        line, column = text_area.index("insert").split(".")
        status_bar.config(text=f"Line {line}, Column {column}")

    text_area.bind("<KeyRelease>", update_status_bar)

    # Define menu functions:
    def zoom_in():
        global font_size
        font_size += 2
        text_area.config(font=("Arial", font_size))

    def zoom_out():
        global font_size
        if font_size > 8:
            font_size -= 2
            text_area.config(font=("Arial", font_size))

    def toggle_status_bar():
        if status_bar.winfo_viewable():
            status_bar.pack_forget()
            viewMenu.entryconfig("Toggle Status Bar", image=root.status_bar_icon, label="Show Status Bar")
        else:
            status_bar.pack(side="bottom", fill="x")
            viewMenu.entryconfig("Toggle Status Bar", image=root.status_bar_icon, label="Hide Status Bar")

    def toggle_word_wrap():
        global word_wrap
        word_wrap = not word_wrap
        text_area.config(wrap="word" if word_wrap else "none")
        viewMenu.entryconfig("Toggle Word Wrap", image=root.word_wrap_icon, label="Disable Word Wrap" if word_wrap else "Enable Word Wrap")

    def run_code():
        code = text_area.get("1.0", "end").strip()
        try:
            output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT, text=True)
            messagebox.showinfo("Output", output)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", e.output)

    # Create View Menu:
    viewMenu = Menu(root, tearoff=0)

    # Add commands with resized icons
    viewMenu.add_command(
        label="Zoom In",
        image=root.zoom_in_icon,
        compound=tk.LEFT,
        accelerator="Ctrl+Plus",
        command=zoom_in
    )
    viewMenu.add_command(
        label="Zoom Out",
        image=root.zoom_out_icon,
        compound=tk.LEFT,
        accelerator="Ctrl+Minus",
        command=zoom_out
    )
    viewMenu.add_separator()
    viewMenu.add_command(
        label="Run",
        image=root.run_icon,
        compound=tk.LEFT,
        accelerator="F5",
        command=run_code
    )
    viewMenu.add_separator()
    viewMenu.add_command(
        label="Toggle Status Bar",
        image=root.status_bar_icon,
        compound=tk.LEFT,
        accelerator="Ctrl+Shift+S",
        command=toggle_status_bar
    )
    viewMenu.add_command(
        label="Toggle Word Wrap",
        image=root.word_wrap_icon,
        compound=tk.LEFT,
        accelerator="Ctrl+Shift+W",
        command=toggle_word_wrap
    )

        # Bind shortcut keys
    root.bind("<Control-=>", lambda event: zoom_in())  # Ctrl+Plus for Zoom In
    root.bind("<Control-Shift-+>", lambda event: zoom_out())  # Ctrl+Shift+Plus for Zoom Out
    root.bind("<F5>", lambda event: run_code())  # F5 for Run
    root.bind("<Control-Shift-S>", lambda event: toggle_status_bar())  # Ctrl+Shift+S for Status Bar Toggle
    root.bind("<Control-Shift-W>", lambda event: toggle_word_wrap())  # Ctrl+Shift+W for Word Wrap Toggle



    return viewMenu