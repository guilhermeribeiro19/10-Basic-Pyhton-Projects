import time

print("Welcome to a Countdown Timer\n")

def countdown():
    seconds = int(input("Enter the amount of seconds: "))
    print("\n Countdown Starts Now:")

    while seconds != 0:
        print('\b'*len(str(seconds)), end='')
        time.sleep(1)
        seconds -= 1
    print("\n CountDown has ended\n")


while True:
    choice = chr(input("Do you want to set a timer: [y] / [n]"))

    if choice == "y":
        countdown()
    elif choice == "n":
        print("Exiting...")
        break
    else:
        print("Please try again")
        break