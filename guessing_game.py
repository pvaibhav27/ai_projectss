import random

print ("\nWelcome to the Guessing Game")
print("I am thinking of a number between 1 and 100")
print("You have 7 attempts to guess the number")

secret = random.randint(1,100)
attempts = 7
while attempts > 0:
    guess = int(input("\nEnter your guess: "))
    if guess == secret:
        print("\nYou guessed the number")
    elif guess > secret:
        print("\nToo high")
    elif guess < secret:
        print("\nToo low")
        attempts -= 1
    if attempts == 0:
        print("\nYou ran out of attempts")
        print("\nThe number was " + str(secret))
        print("Better luck next time")
print("Thanks for playing")