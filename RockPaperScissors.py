import random
import tkinter as tk
#Create variables for rock, paper, and scissors

#Generate rps randomly

#Rock > Scissors, Scissors > Paper, Paper > Rock

#Get user input



counter = 0
win = 0
lose = 0
while counter < 3:

    user = input("Select 'rock', 'paper', or 'scissors': ")
    possible_actions = ['rock', 'paper', 'scissors']
    comp = random.choice(possible_actions)
    print(f"You chose {user}, and the computer chose {comp}.")

    if comp == user:
        print("It's a tie!")
        print(f"Overall record is: {win}-{lose}.")
    if user == 'rock':
        if comp == 'paper':
            print("You lose.")
            counter -= 1
            lose += 1
            print(f"Overall record is: {win}-{lose}.")
        elif comp == 'scissors':
            print("You win!")
            counter += 1
            win += 1
            print(f"Overall record is: {win}-{lose}.")
    if user == 'scissors':
        if comp == "rock":
            print("You lose.")
            counter -= 1
            lose += 1
            print(f"Overall record is: {win}-{lose}.")
        elif comp == 'paper':
            print("You win!")
            counter += 1
            win += 1
            print(f"Overall record is: {win}-{lose}.")
    if user == 'paper':
        if comp == 'rock':
            print("You win!")
            counter += 1
            win += 1
            print(f"Overall record is: {win}-{lose}.")
        elif comp == 'scissors':
            print("You lose.")
            counter -= 1
            lose += 1
            print(f"Overall record is: {win}-{lose}.")



