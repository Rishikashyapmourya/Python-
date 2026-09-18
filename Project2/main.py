import random

computer = random.randint(1, 100)

while True:
    number = int(input("Guess the number :"))

    if (number > computer):
        print("Lower number please  ")
    elif (number< computer):
        print("Higher number please")
    else:
        print("Your Win!")
        break

print(f"Computer number was:{computer}")


