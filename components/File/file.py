import tkinter as tk
from tkinter import Menu, filedialog, messagebox

# Define Function For File Menu:
def File(root):
    # Create File Menu:
    menu = Menu(root)
    fileMenu = Menu(menu, tearoff=0)

    # Define functions for menu actions:
    def new_file():
        text_area.delete("1.0", "end")
        root.title("Untitled - Notepad")

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                text_area.delete("1.0", "end")
                text_area.insert("1.0", file.read())
            root.title(f"{file_path} - Notepad")

    def open_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            messagebox.showinfo("Open Folder", f"Opened folder: {folder_path}")

    def recent_files():
        messagebox.showinfo("Recent Files", "No recent files available.")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", "end"))
            root.title(f"{file_path} - Notepad")

    def save_as_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", "end"))
            root.title(f"{file_path} - Notepad")

    def exit_app():
        root.quit()

    # Add options to File menu:
    fileMenu.add_command(label="New File", command=new_file)
    fileMenu.add_command(label="Open File", command=open_file)
    fileMenu.add_command(label="Open Folder", command=open_folder)
    fileMenu.add_command(label="Recent Files", command=recent_files)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save", command=save_file)
    fileMenu.add_command(label="Save As", command=save_as_file)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exit_app)

    menu.add_cascade(label="File", menu=fileMenu)
    root.config(menu=menu)

    # Create a text area:
    global text_area
    text_area = tk.Text(root, wrap="word", undo=True)
    text_area.pack(expand=1, fill="both")
