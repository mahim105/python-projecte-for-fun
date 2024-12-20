import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            messagebox.showinfo("Winner!", f"Player {buttons[combo[0]]['text']} wins!")
            reset_game()
            return

def reset_game():
    for button in buttons:
        button.config(text="")
    global current_player
    current_player = "X"  # Reset to player X

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
current_player = "X"

for i in range(9):
    button = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

def on_button_click(i):
    global current_player  # Declare current_player as global before using it
    if buttons[i]['text'] == "":
        buttons[i]['text'] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

root.mainloop()

