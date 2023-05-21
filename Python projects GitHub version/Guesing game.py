import random

print("Guess the amount of money:")

number = random.randint(1, 10)
guesses = 0

while True:
    guess = int(input("Enter your guess (between 1 and 10): "))
    guesses += 1

    if guess == number:
        print("Congratulations, you guessed the correct amount!")
        print("Number of guesses:", guesses)
        break

    elif guess < number:
        print("Your guess is too low, try again.")

    else:
        print("Your guess is too high, try again.")
