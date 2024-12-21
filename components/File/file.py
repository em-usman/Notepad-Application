import tkinter as tk
from tkinter import Menu, filedialog, messagebox
import os

def File(root, text_area):
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

    # File icons
    try:
        new_icon = load_icon('new.png')
        open_icon = load_icon('open.png')
        save_icon = load_icon('save.png')
        save_as_icon = load_icon('save_as.png')
        exit_icon = load_icon('exit.png')
    except FileNotFoundError as e:
        print(e)
        messagebox.showerror("Icon Error", f"An error occurred while loading icons:\n{e}")
        return

    # Keep a reference to the icons for Tkinter menu
    root.new_icon = new_icon
    root.open_icon = open_icon
    root.save_icon = save_icon
    root.save_as_icon = save_as_icon
    root.exit_icon = exit_icon

    # Variable to store the current file path
    url = ''
    text_changed = False

    # New functionality
    def new_file(event=None):
        nonlocal url, text_changed
        url = ''
        text_area.delete(1.0, tk.END)
        text_changed = False
        root.title("Untitled - Notepad")

    # Open functionality
    def open_file(event=None):
        nonlocal url
        url = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title='Select File',
            filetypes=(('Text File', '*.txt'), ('All files', '*.*'))
        )
        try:
            with open(url, 'r') as fr:
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, fr.read())
                root.title(os.path.basename(url))
        except FileNotFoundError:
            return
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")

    # Save functionality
    def save_file(event=None):
        nonlocal url
        try:
            if url:
                content = text_area.get(1.0, tk.END)
                with open(url, 'w', encoding='utf-8') as fw:
                    fw.write(content)
            else:
                save_as()
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")

    # Save as functionality
    def save_as(event=None):
        nonlocal url
        try:
            content = text_area.get(1.0, tk.END)
            url = filedialog.asksaveasfile(
                mode='w',
                defaultextension='.txt',
                filetypes=(('Text File', '*.txt'), ('All files', '*.*'))
            )
            if url:
                url.write(content)
                url.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")

    # Exit functionality
    def exit_func(event=None):
        nonlocal url, text_changed
        try:
            if text_changed:
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
                if mbox is True:
                    if url:
                        content = text_area.get(1.0, tk.END)
                        with open(url, 'w', encoding='utf-8') as fw:
                            fw.write(content)
                            root.destroy()
                    else:
                        save_as()
                        root.destroy()
                elif mbox is False:
                    root.destroy()
            else:
                root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error while closing the application: {e}")

    # Create the File menu (ensure it is a correct menu object)
    file_menu = Menu(root, tearoff=0)

    # Add commands with resized icons
    file_menu.add_command(
        label='New',
        image=root.new_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+N',
        command=new_file
    )
    file_menu.add_command(
        label='Open',
        image=root.open_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+O',
        command=open_file
    )
    file_menu.add_command(
        label='Save',
        image=root.save_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+S',
        command=save_file
    )
    file_menu.add_command(
        label='Save As',
        image=root.save_as_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+Alt+S',
        command=save_as
    )
    file_menu.add_separator()
    file_menu.add_command(
        label='Exit',
        image=root.exit_icon,
        compound=tk.LEFT,
        accelerator='Ctrl+Q',
        command=exit_func
    )
    
    ##bindi shortcut keys
    root.bind("<Control-n>", new_file)
    root.bind("<Control-o>", open_file)
    root.bind("<Control-s>", save_file)
    root.bind("<Control-Alt-s>", save_as)
    root.bind("<Control-q>", exit_func)
    root.bind("<Control-q>", exit_func)

    return file_menu
