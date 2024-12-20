import tkinter as tk 
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[('Text Files', '*.txt')])  # Fixed spelling and file extension
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])  # Fixed file extension
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo('Info', 'File saved successfully')  # Fixed typo

root = tk.Tk()
root.title('Simple Text Editor')
root.geometry('800x600')

menu = tk.Menu(root)  # Fixed spelling from 'manu' to 'menu'
root.config(menu=menu)  # Fixed spelling from 'manu' to 'menu'
file_menu = tk.Menu(menu)  # Fixed spelling from 'file_manu' to 'file_menu'
menu.add_cascade(label='File', menu=file_menu)  # Fixed spelling from 'file_manu' to 'file_menu'
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)  # Capitalized 'Save'
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 12), fg='blue')
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
