import secrets
import random

print("Welcome to PAN!")

r = random
score = 0
guess = 0
count = 1

levels = ('easy', 'intermediate', 'hard')
print(levels)
 

print (input("Enter P to play"))

print(" Welcome to level 1: Easy")

print("Pick a number between 1 and 10")
random = random.randint(1,10) 


while guess != random:
    guess = int(input("Pick a number "))

    if guess > random:
        print("Too high")
        count += 1

    if guess < random:
        print("Too low")
        count += 1

    if guess == random:
        print("Correct")
        score += 10
        break

print("It took you", count, "tries to make it to level 2")
print("Your score is now",score)

print("Welcome to level 2: Intermediate")

score = 10
guess2 = 0
count2 = 1


secrets = secrets.randbelow(50) 
print("Pick a number between 1 and 50")

while guess2 != random:
    guess2 = int(input("Pick a number "))

    if guess2 > random:
        print("Too high")
        count2 += 1

    if guess2 < random:
        print("Too low")
        count2 += 1

    if guess2 == random:
        print("Correct")
        score += 10
        break

print("It took you", count2, "tries to make it to level 3")
print("Your score is now",score)

print("Welcome to level 3: Hard")

score = 20
guess3 = 0
count3 = 1

print("Pick a number between 1 and 100")
import random 
random = random.randint(1,100)

while guess3 != random:
    guess3 = int(input("Pick a number "))

    if guess3 > random:
        print("Too high")
        count3 += 1

    if guess3 < random:
        print("Too low")
        count3 += 1

    if guess3 == random:
        print("Correct")
        score += 10
        break

print("It took you", count3, "tries to complete level 3")
print("Your score is now..",score)
