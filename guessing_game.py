# Create a guessing game where user guesses a randomized number between 1 and 10 and if the user's guess is high or low.
# Also use a guess counter, if guess > 6 then user loses
import random
guessCount = 0
print("\nHello, What is your name? ")
name = input()

print("Let's play a guessing game, " + str(name) + ", Guess a Number between 1 and 20! ")
print("You only get 4 tries! ")

randNum = random.randint(1,20)

for i in range(8):
    if guessCount < 4:
        print("\nTake a guess: ")
        guess = int(input())

        if guess > randNum:
            print("Your guess is too high! Try Lower: ")
            guessCount = guessCount + 1
        elif guess < randNum:
            print("Your Guess is too low! Try again: ")
            guessCount = guessCount + 1
        else:
            print("\nYour guess is correct!")
            guessCount = guessCount + 1
            print("It took you " + str(guessCount) + " tries!")
            break
        
    else:
        print("\nYou ran out of tries :( ")
        print("The number was " + str(randNum))
        break
