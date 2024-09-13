import string
import getpass


def check_length(password):
    strength =0

    if len(password) <=10:
        print("The password must have at least 10 characters.")
        return strength, True
    elif len(password) > 10 and len(password) <= 20:
        strength +=1
    elif len(password) > 20:
        strength +=2
    
    return strength, False

def check_uppercase(password):
    strength = 0
    count_upper = 0

    for char in password:
        if char.isupper():
            count_upper +=1

    if count_upper > 3:
        strength +=1
    elif count_upper == 0:
        print("The password must have at least 1 upper case character.")
        return strength, True
    
    return strength, False

def check_lowercase(password):
    
    count_lower = 0

    for char in password:
        if char.islower():
            count_lower +=1

    if count_lower == 0:
        print("The password must have at least 1 lower case character.")
        return strength, True

    return strength, False

def check_special_char(password):
    strength = 0
    special_characters = string.punctuation  

    count_special = 0
    for char in password:
        if char in special_characters:
            count_special += 1

    if count_special >= 1:
        strength += 1
    else:
        print("The password must have at least 1 special character.")
        return strength, True 

    return strength, False  

def check_sequential_chars(password):
    strength = 0
    sequences = ["1234", "2345", "3456", "4567", "5678", "6789", 
                 "abcd", "bcde", "cdef", "defg", "efgh", "fghi", 
                 "ghij", "hijk", "ijkl", "jklm", "klmn", "lmno", 
                 "mnop", "nopq", "opqr", "pqrs", "qrst", "rstu", 
                 "stuv", "tuvw", "uvwx", "vwxy", "wxyz"]

    found_sequence = False
    for seq in sequences:
        if seq in password:
            found_sequence = True
            break

    if found_sequence:
        print("The password contains sequential characters, which can make it easier to guess.")
        return strength, True  
    else:
        strength += 1

    return strength, False


print("\nWelcome to a Password Strength Checker")

while True:
    choice = input("Do you want to proceed: (y/n) ")
    if choice == "y":
        password = getpass.getpass("Enter your password: ")
        total_strength = 0
        restart = False
        
        checks = [check_length, check_uppercase, check_lowercase, check_special_char, check_sequential_chars]
            
        for check in checks:
            strength, restart_flag = check(password)
            total_strength += strength
            if restart_flag:
                restart = True
                break
            
        if restart:
                continue  
            
        if total_strength >= 0 and total_strength < 2:
            print("\nThat's a very bad password. Change it as soon as possible.")
        elif total_strength >= 2 and total_strength < 4:
            print("Your password is hard to guess. But you can make it even more secure")
        elif total_strength > 5:
            print("The password is very secure")


    elif choice == "n":
        print("\nExiting...")
        break

    else:
        print("\nSomething went wrong, please try again")
        break
