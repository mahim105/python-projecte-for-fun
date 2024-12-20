import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo('Info', 'File saved successfully')

def change_bg_color(color):
    text.config(bg=color)

def change_fg_color(color):
    text.config(fg=color)

root = tk.Tk()
root.title('Simple Text Editor')
root.geometry('800x600')

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Color selection
color_menu = tk.Menu(menu)
menu.add_cascade(label='Colors', menu=color_menu)

bg_colors = ['white', 'yellow', 'light blue', 'light green', 'pink','black']
fg_colors = ['black', 'blue', 'red', 'green', 'purple']

# Dropdown for background color
bg_var = tk.StringVar(value=bg_colors[0])
bg_option_menu = tk.OptionMenu(root, bg_var, *bg_colors, command=change_bg_color)
bg_option_menu.pack(side=tk.LEFT, padx=5)

# Dropdown for text color
fg_var = tk.StringVar(value=fg_colors[0])
fg_option_menu = tk.OptionMenu(root, fg_var, *fg_colors, command=change_fg_color)
fg_option_menu.pack(side=tk.LEFT, padx=5)

text = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 12), fg='black', bg='white')
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
