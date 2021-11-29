import random

options = ("rock", "paper", "scissors")
random = random.choice(options)

print("Welcome to RPS. Please enter rock, paper, or scissors")


player = input()

while True:
    if player == 'rock':
        print(random)

    if player == 'paper':
        print(random)

    if player == "scissors":
        print(random)

    if player == random:
        print("There was a tie")
    break
