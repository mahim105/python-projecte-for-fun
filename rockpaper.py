import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f'Computer chose: {computer_choice}\n{result}')

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=('Helvetica', 16))
result_label.pack(pady=20)

# Run the application
root.mainloop()
