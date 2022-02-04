# Rock Paper Scissors game by Caroline C (student)

# Futurelearn Course: Programming Applications with Python Graphics User Interface
# Week 2.6: Offline Activity Create your GUI

# Objective: "Use all of your new-found knowledge about GUI programming
# to create something simple, yet functional. Try and incorporate all
# the elements that you learned up until now."

import tkinter as tk  # Import the GUI library
import tkinter.messagebox
from PIL import Image, ImageTk  # Pillow library
import random  # Import random choice library

window = tk.Tk()  # Create window
window.title('Rock Paper Scissors Game')  # Set window title
window.geometry('600x400+450+200')  # Set window size and X and Y positioning

label1 = tk.Label(text='Would you like to play a game?\n\nChoose rock, paper, or scissors!\n')
label1.pack()


def rps():
    x = random.randint(0, 2)  # Generate random integer between 0 and 2
    if gameVar.get() == 0 and x == 0:
        tk.messagebox.showinfo('Result', 'Draw!')
    elif gameVar.get() == 0 and x == 1:  # Player picks rock and computer picks paper
        tk.messagebox.showinfo('Result', 'Lose!')
    elif gameVar.get() == 0 and x == 2:  # Player picks rock and computer picks scissors
        tk.messagebox.showinfo('Result', 'Win!')
    elif gameVar.get() == 1 and x == 1:
        tk.messagebox.showinfo('Result', 'Draw!')
    elif gameVar.get() == 1 and x == 0:  # Player picks paper and computer picks rock
        tk.messagebox.showinfo('Result', 'Win!')
    elif gameVar.get() == 1 and x == 2:  # Player picks paper and computer picks scissors
        tk.messagebox.showinfo('Result', 'Lose!')
    elif gameVar.get() == 2 and x == 2:
        tk.messagebox.showinfo('Result', 'Draw!')
    elif gameVar.get() == 2 and x == 1:  # Player picks scissors and computer picks paper
        tk.messagebox.showinfo('Result', 'Win!')
    elif gameVar.get() == 2 and x == 0:  # Player picks scissors and computer picks rock
        tk.messagebox.showinfo('Result', 'Lose!')


gameVar = tk.IntVar(window, value=0)
rock = tk.Radiobutton(window, text='Rock', value=0, variable=gameVar)  # Default selection
paper = tk.Radiobutton(window, text='Paper', value=1, variable=gameVar)
scissors = tk.Radiobutton(window, text='Scissors', value=2, variable=gameVar)
rock.pack()
paper.pack()
scissors.pack()
play = tk.Button(window, text='Play Game!', command=rps)
play.pack()

# Image credit: Image by OpenClipart-Vectors from Pixabay
# Image source: https://pixabay.com/vectors/fingers-fist-hands-paper-rock-149295/
image = Image.open('hands.png')  # Select image
image = image.resize((240, 165), Image.ANTIALIAS)  # Resize image
hands = ImageTk.PhotoImage(image)  # Assign image to variable
label2 = tkinter.Label(image=hands)
label2.place(x=180, y=200)

window.mainloop()
