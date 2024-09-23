#!/usr/bin/env python3

'''
Course: Programming Applications with Python Graphics User Interface
Student Name: Caroline Lau Campbell

Assignment: 
Week 2.6 Offline Activity Create your GUI
Use all of your new-found knowledge about GUI programming to create something 
simple, yet functional. Try and incorporate all the elements that you learned 
up until now.

NB: This is the rock-paper-scissors game that I wrote for my Futurelearn 
course (2022). I have refreshed it to reflect my gain in knowledge from 
subsequent courses with Edgehill Uni (2022) and the Open University (2024).
'''

import tkinter as tk  # Tkinter GUI library.
import tkinter.messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow library.
import random  # Random choice library.

### Winning combos ###
winning_combinations = [
    (0, 2), # Rock beats scissors.
    (1, 0), # Paper beats rock.
    (2, 1)  # Scissors beats paper.
]

game_tokens = {0: 'rock',
               1: 'paper',
               2: 'scissors'}

game_counter = 0 # Number of games played.
win_counter = 0 # Number of games won by player.

def play_game():
    """Get player choice, generate computer choice, check if the player won,
    update game_counter and win_counter, display result in popup, and update 
    the count_msg with the tallies.
    """    
    global game_counter, win_counter
    ### Computer move ###
    computer_choice = random.randint(0, 2) # Random int 0 to 2.
    ### Player move ###
    player_choice = selected_choice.get()
    ### Check for win ###
    if player_choice == computer_choice:
        result = "Draw!"
    elif (player_choice, computer_choice) in winning_combinations:
        result = "Win!"
        win_counter = win_counter+1
    else:
        result = "Lose!"
    game_counter = game_counter+1
    result_msg = f'''You chose {game_tokens[player_choice]}.
The computer chose {game_tokens[computer_choice]}.
Your result is... {result}'''
    tk.messagebox.showinfo('Result', result_msg)
    count_msg = f'''You have played {game_counter} games.
You have won {win_counter} times!
    '''
    count_label.config(text=count_msg)

root = tk.Tk() # Create window.
root.title('Rock Paper Scissors Game') # Set window title.
root.geometry('600x500+450+200') # Set window size and X and Y positioning.
style = ttk.Style()
style.configure('.', font= ('Courier', 16))
style.configure('TLabel', wraplength=550)

msg_to_player = '''Would you like to play a game? \
Choose rock, paper or scissors and click the play button. \
Rock beats scissors, scissors beats paper, and paper beats rock!'''
instructions = ttk.Label(root, text=msg_to_player)
instructions.grid(row=0, columnspan=3, padx=10, pady=10)

# Image credit: Image by OpenClipart-Vectors from Pixabay
# Image source: https://pixabay.com/vectors/fingers-fist-hands-paper-rock-149295/
image = Image.open('hands.png') # Select image.
image = image.resize((240, 165), resample=Image.Resampling.BICUBIC) # Resize image.
hands = ImageTk.PhotoImage(image) # Assign image to variable.
label2 = tkinter.Label(image=hands)
label2.grid(row=1, columnspan=3)

selected_choice = tk.IntVar(root, value=0) # Default player choice is 0.

choices = ttk.LabelFrame(root, text='Player choices:')
rock = ttk.Radiobutton(choices, text='Rock', 
                       variable=selected_choice, value=0) # Default selection.
paper = ttk.Radiobutton(choices, text='Paper', 
                        variable=selected_choice, value=1)
scissors = ttk.Radiobutton(choices, text='Scissors', 
                           variable=selected_choice, value=2)
rock.pack(side=tk.LEFT)
paper.pack(side=tk.LEFT)
scissors.pack(side=tk.LEFT)
choices.grid(row=2, columnspan=3, padx=10, pady=10, sticky='nsew')

play_button = ttk.Button(root, text='Play Game!', command=play_game)
play_button.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
quit_button = ttk.Button(root, text='Quit', command=lambda: root.quit())
quit_button.grid(row=4, column=2, padx=10, pady=10, sticky='nsew')

count_msg = f'''You have played {game_counter} games.
You have won {win_counter} times!
'''
count_label = ttk.Label(root, text=count_msg)
count_label.grid(row=5, columnspan=3, padx=10, pady=10, sticky='nsew')

root.mainloop()