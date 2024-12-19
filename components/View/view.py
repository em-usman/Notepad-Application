from tkinter import Menu, Text, Label, simpledialog, messagebox
import tkinter as tk
import subprocess

# Define function for View Menu:
def View(root, text_area):
    global font_size, status_bar, word_wrap
    font_size = 12
    word_wrap = True

    # Define status bar:
    status_bar = Label(root, text="Line 1, Column 1", anchor="e")
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
        else:
            status_bar.pack(side="bottom", fill="x")

    def toggle_word_wrap():
        global word_wrap
        word_wrap = not word_wrap
        text_area.config(wrap="word" if word_wrap else "none")

    def search_text():
        search_query = simpledialog.askstring("Search", "Enter text to search:")
        if search_query:
            start = "1.0"
            while True:
                start = text_area.search(search_query, start, stopindex="end")
                if not start:
                    break
                end = f"{start}+{len(search_query)}c"
                text_area.tag_add("highlight", start, end)
                text_area.tag_config("highlight", background="yellow")
                start = end
            messagebox.showinfo("Search Completed", f"Search for '{search_query}' completed.")

    def run_code():
        code = text_area.get("1.0", "end").strip()
        try:
            output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT, text=True)
            messagebox.showinfo("Output", output)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", e.output)

    # Create View Menu:
    viewMenu = Menu(root, tearoff=0)
    viewMenu.add_command(label="Zoom In", command=zoom_in)
    viewMenu.add_command(label="Zoom Out", command=zoom_out)
    viewMenu.add_separator()
    viewMenu.add_command(label="Toggle Status Bar", command=toggle_status_bar)
    viewMenu.add_command(label="Toggle Word Wrap", command=toggle_word_wrap)
    viewMenu.add_separator()
    viewMenu.add_command(label="Search", command=search_text)
    viewMenu.add_command(label="Run", command=run_code)

    return viewMenu