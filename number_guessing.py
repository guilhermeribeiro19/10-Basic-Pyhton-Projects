import random

def get_random_number():
    number = random.randint(1,100)
    return number

print("\nWelcome to the Try to Guess the Number Game!")



while True:
    choice = input("\nDo you want to Guess the Number? (y/n) ")

    number_to_guess = get_random_number()
    chances = 5
    if choice == "y":

        while chances > 0:
            print(f"\nYou have {chances} chances to get it right")

            guess = int(input("\nChoose a number between 1 and 100:  "))

            if guess == number_to_guess:
                print("You got the number right!")
                break

            elif guess < number_to_guess:
                print("\nThe number you choose is lower than the number we choose, try again...")

            elif guess > number_to_guess:
                print("\nThe number you choose is higher than the number we choose, try again...")

            elif guess > 100:
                print("Invalid input...please try again")

            chances -= 1

            print("You lost, feel free to try again!")

    elif choice == "n":
        print("\nExiting...")
        break

    else:
        print("\nSomething went wrong, please try again")
        break
        