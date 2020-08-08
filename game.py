# This is a Guess the Number game.
## Please do Debug, if player type string, it will cause error ##

import random

guessTaken = 0

print("Hello! What is your name?")
myName = input()

number = random.randint(2, 20)

print('DEBUG: Number is' + ' ' + str(number)) # Debug 

print('Well, ' + myName + ', I am thinkiung of a number between 1 and 20.' )


for guessesTaken in range(6):
    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high')
    else:
        break # This condition is for the correct guess!

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job,' + ' ' + myName + '! You guessed my number in' + ' ' + str(guessesTaken) + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + str(number) + '.')
