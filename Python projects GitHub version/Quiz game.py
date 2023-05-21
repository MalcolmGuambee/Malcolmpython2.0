
input("Welcome to Malcolm Quiz")
Name = input("What is your name?: ")

while Name.isdigit():
    Name = input("what is your name:")

else:Name.isalpha()
print("You will get 100 MT if you complete it.")
print("Remainder before starting: Put a space in each word when writing long answers.")

playing = input("Do you want to play? Y/N: ")
if playing.upper() == "N":
    print("No game:", Name)
    quit()

print("Are you ready,", Name)

if playing.upper() != "Y":
    quit()

print("Okay! Let's play :)")

answer = input("Where was Adolf Hitler born? ")
if answer.lower() == "germany":
    print("Correct")
else:
    print("Wrong")


answer2 = input("Who discovered Brazil? ")
if answer2.lower() == "pedro alvares cabral":
    print('You are right')
else:
    print("Wrong")


answer3 = input("Which language has the most native speakers? ")
if answer3.lower() == "spanish":
    print('Marvellous')
else:
    print("Wrong")


answer4 = input("How many ghosts chase Pac-Man at the start of each game? ")
if answer4.lower() == "4":
    print('Outstanding')
else:
    print("Wrong")


answer5 = input("What country has won the most World Cups? ")
if answer5.lower() == "brazil":
    print('Fantastic')
else:
    print("Wrong")


answer6 = input("Finish the lyrics: I got... ")
if answer6.lower() == "ninty-nine problems but a bitch ain't one":
    print('Amazing')
else:
    print("Wrong")


answer7 = input("In what country was Elon Musk born? ")
if answer7.lower() == "south africa":
    print('You are Beguilling')
else:
    print("Wrong")


answer8 = input("Where is Disney's European theme park located? ")
if answer8.lower() == "france":
    print('You are right')
else:
    print("Wrong")


answer9 = input("What color are Mickey Mouse's shoes? ")
if answer9.lower() == "yellow":
    print('You are right')
else:
    print("Wrong")


answer10 = input("What does PSU stand for? ")
if answer10.lower() == "power supply unit":
    print('You are right')
else:
    print("Wrong")

print("Wow! You made it!")
print("Do you eant to play again:Y/N")
if playing.upper() == "N":
    print("Ok :")
    quit()
print("Are you ready,", Name)





























