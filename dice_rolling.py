import random

def roll_dice():
    dice_number = random.randint(1,6)
    return dice_number

print("\nWelcome to a Dice Roller")

while True:
    i = input("Do you want to role the dice: (y/n)  ")

    if i == "y":
        print("Rolling dice...", roll_dice())

    elif i == "n":
        print("Exiting...")
        break

    else:
        print("There was an error, please try again...")
        break