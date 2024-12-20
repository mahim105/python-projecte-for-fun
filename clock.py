import tkinter as tk 
from time import strftime 

root = tk.Tk()  # Use Tk() with a capital 'T'
root.title('Digital Clock')

def time():
    string = strftime('%H:%M:%S %p \n %D')  # Correct the format string
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('Calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()  # Call the time function to start the clock

root.mainloop()
