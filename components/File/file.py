from tkinter import Menu, filedialog, messagebox

def File(root, text_area):
    def new_file():
        text_area.delete("1.0", "end")

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                text_area.delete("1.0", "end")
                text_area.insert("1.0", file.read())

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", "end"))

    def exit_app():
        root.quit()

    fileMenu = Menu(root, tearoff=0)
    fileMenu.add_command(label="New", command=new_file)
    fileMenu.add_command(label="Open", command=open_file)
    fileMenu.add_command(label="Save", command=save_file)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exit_app)

    return fileMenu
