#logical operator (and,or,not) = used to check if two or more conditional statements is true
# not turns a flase stament into true and vice versa

score = int(input("How much did you score?:"))

if score >= 75 and score <=100 :
    print("Excelleenttt")
    print("Great! ")
elif score < 0 or score  > 50:
    print("TryHardNextTime")
    print("Bad")
