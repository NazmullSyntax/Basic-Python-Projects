import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = input("Choose rock, paper, or scissors: ").lower()

if player == computer:
    print("Tie!")
elif (player == 'rock' and computer == 'scissors') or \
     (player == 'paper' and computer == 'rock') or \
     (player == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("You lose!")