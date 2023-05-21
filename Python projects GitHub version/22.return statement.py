# return statement = Functions send Python values/objects back to the caller.

#                    These values/objects are known as the function’s return value



#def multiply(number1,number2):

    #return number1 * number2



#x = multiply(6,8)



#print(x)

import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1, 20)
guesses = 0

while guesses < 3:
    guess = int(input("Guess a number between 1 and 20: "))
    guesses += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations, you guessed the number!")
        break

if guesses == 3:
    print("Sorry, you ran out of guesses. The number was", number)
