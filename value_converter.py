def convert_temp():
    print("\nWhich conversion do you want to do?")
    print("1. Celsius to Faranheit")
    print("2. Faranheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter the Temperature: "))
        print(f"{temp} degree celsius is equal to {round((temp*9/5)+32,2)} degree faranheit.\n")

    elif choice == 2:
        temp = float(input("Enter the Temperature: "))
        print(f"{temp} degree faranheit is equal to {round((temp-32)*5/9,2)} degree celsius.\n")

    else:
        print("Invalid input...please try again\n")
              
def convert_curr():
    print("\nWhich conversion do you want to do?")
    print("1. Dollars to Euro")
    print("2. Euro to Dollars")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        curr = float(input("Enter the Amount: "))
        print(f"{curr} in dollars is equal to {round((curr*0.91), 2)} in euro")
    elif choice == 2:
        curr = float(input("Enter the Amount: "))
        print(f"{curr} in euro is equal to {round((curr/0.91),2)} in dollars")
    else:
        print("Invalid input...please try again\n")

def convert_measure():
    print("\nWhich conversion do you want to do?")
    print("1. Centimeters to Foot and Inches")
    print("2. Foot and Inches to Centimeters")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        meas = float(input("Enter the Measure: "))
        inches = meas/2.54
        feet = inches/12
        print(f"{meas} centimeters in equal to {round(feet,2)} feet and {round(inches, 2)} inch\n")

    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        inches = float(input("Enter length in inches: "))
        meas = (feet*12 + inches)*2.54
        print(f"{feet} feet and {round(inches,2)} inches in centimeters will be {round(meas,2)}\n")
    else:
        print("Invalid input...please try again\n")

print("\nWelcome to the Value Converter")

while True:
    convert = input("\nDo you want to Convert something? (y/n)  ")
    if convert == "y":
        print("Which option would you like to choose:-")
        print("1. Convert temperature")
        print("2. Convert currency")
        print("3. Convert measure")
        print("4. Exit")
        option = int(input("Enter your choice: "))
        if option == 1:
            convert_temp()
        elif option == 2:
            convert_curr()
        elif option == 3:
            convert_measure()
        else:
            print('Exiting...')
            break

    elif convert == "n":
        print("\nExiting...")
        break

    else:
        print("\nSomething went wrong, please try again")
        break
