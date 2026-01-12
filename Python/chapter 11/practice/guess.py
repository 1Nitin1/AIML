import random as r
number = r.randint(1, 100)
guess=0
n=int(input("Guess a number between 1 to 100: "))
while(guess!=number):
    guess+=1
    if n<number:
        print("Too low!")
        n=int(input("Guess a number between 1 to 100: "))
    elif n>number:
        print("Too high!")
        n=int(input("Guess a number between 1 to 100: "))
    else:
        print(f"You guessed it right! and took {guess} attempts")
        break