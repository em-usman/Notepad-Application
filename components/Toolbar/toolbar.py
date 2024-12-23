import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser, font


import tkinter as tk
from tkinter import ttk, colorchooser, font

def toolbar(root, text_area):
    # Toolbar setup
    tool_bar = ttk.Label(root)
    tool_bar.pack(side=tk.TOP, fill=tk.X)
    text_area.pack(expand=1, fill="both")

    # Font Box
    font_tuple = font.families()
    font_family = tk.StringVar()
    font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
    font_box['values'] = font_tuple
    font_box.current(font_tuple.index('Arial'))
    font_box.grid(row=0, column=0, padx=5)

    # Size Box
    size_var = tk.IntVar()
    font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
    font_size['values'] = tuple(range(8, 80, 2))
    font_size.current(4)
    font_size.grid(row=0, column=1, padx=5)

    # Toolbar Buttons
    button_configs = [
        ("icons2/bold.png", 2, lambda: change_style('weight', 'bold')),
        ("icons2/italic.png", 3, lambda: change_style('slant', 'italic')),
        ("icons2/underline.png", 4, lambda: underline_text()),
        ("icons2/font_color.png", 5, lambda: change_font_color()),
        ("icons2/align_left.png", 6, lambda: align_text('left')),
        ("icons2/align_center.png", 7, lambda: align_text('center')),
        ("icons2/align_right.png", 8, lambda: align_text('right')),
    ]

    for icon_path, col, command in button_configs:
        icon = tk.PhotoImage(file=icon_path).subsample(2, 2)
        button = ttk.Button(tool_bar, image=icon, command=command)
        button.image = icon  # Keep a reference to avoid garbage collection
        button.grid(row=0, column=col, padx=5)

    # Global variables for font and size
    current_font_family = 'Arial'
    current_font_size = 12

    def change_font(event=None):
        nonlocal current_font_family
        current_font_family = font_family.get()
        text_area.config(font=(current_font_family, current_font_size))

    def change_size(event=None):
        nonlocal current_font_size
        current_font_size = size_var.get()
        text_area.config(font=(current_font_family, current_font_size))

    font_box.bind("<<ComboboxSelected>>", change_font)
    font_size.bind("<<ComboboxSelected>>", change_size)

    # Change text style (bold/italic)
    def change_style(style_attr, style_value):
        text_property = font.Font(font=text_area['font'])
        current_value = text_property.actual().get(style_attr)
        if current_value != style_value:
            text_area.config(font=(current_font_family, current_font_size, style_value))
        else:
            text_area.config(font=(current_font_family, current_font_size, 'normal'))

    # Underline text
    def underline_text():
        text_property = font.Font(font=text_area['font'])
        if not text_property.actual()['underline']:
            text_area.config(font=(current_font_family, current_font_size, 'underline'))
        else:
            text_area.config(font=(current_font_family, current_font_size, 'normal'))

    # Change font color
    def change_font_color():
        color = colorchooser.askcolor()[1]
        if color:
            text_area.config(fg=color)

    def align_text(align_type):
        text_area.tag_configure(align_type, justify=align_type)  # Configure the tag with the desired justification
        text_content = text_area.get(1.0, tk.END)  # Get all the text
        text_area.delete(1.0, tk.END)  # Clear the text area
        text_area.insert(tk.INSERT, text_content)  # Reinsert the text
        text_area.tag_add(align_type, "1.0", tk.END)  # Apply the tag to all text


    return tool_bar
