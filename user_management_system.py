database = {'entries': []}

SRNO = 'srno'
NAME = 'name'
AGE = 'age'
GENDER = 'gender'
OCCUPATION = 'occupation'

def get_serial_number():
    return len(database['entries']) + 1

def add_entry(entry):
    entry = {
        'srno': get_serial_number(),
        'name': entry['name'],
        'age': entry['age'],
        'gender': entry['gender'],
        'occupation': entry['occupation']
    }
    database['entries'].append(entry)

def check_entry_presence(value):
    for entry in database['entries']:
        if entry.get(value[0]) == value[1]:
            return True
    return False

def search_entry(value):
    for entry in database['entries']:
        if entry.get(value[0]) == value[1]:
            return entry
        
def update_entry(value, updated_entry):
    for i, entry in enumerate(database['entries']):
        if entry.get(value[0]) == value[1]:
            database['entries'][i] = updated_entry
            break

def delete_entry(value):
    for entry in database['entries']:
        if entry.get(value[0]) == value[1]:
            database['entries'].remove(entry)
        break

def display_entry(entry):
    print(f"SRNO: {entry['srno']}")
    print(f"Name: {entry['name']}")
    print(f"Age: {entry['age']}")
    print(f"Gender: {entry['gender']}")
    print(f"Occupation: {entry['occupation']}\n")


def display_all_entries():
    for entry in database['entries']:
        display_entry(entry)

def select_entry_and_value():
    print('Choose an entry based on which to search entries in the database:')
    print("1. srno")
    print("2. name")
    print("3. age")
    print("4. gender")
    print("5. occupation")
    while True:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            print("Invalid input...please try again")
        else:
            break
    if choice == 1:
        value_type = SRNO
        value = input("Enter serial number to search: ")
    elif choice == 2:
        value_type = NAME
        value = input("Enter name to search: ")
    elif choice == 3:
        value_type = AGE
        value = input("Enter age to search: ")
    elif choice == 4:
        value_type = GENDER
        value = input("Enter gender to search: ")
    elif choice == 5:
        value_type = OCCUPATION
        value = input("Enter occupation to search: ")
    return (value_type, value)

def get_entry_details():
    output = {}
    output[NAME] = input("Enter name: ")
    output[AGE] = input("Enter age: ")
    output[GENDER] = input("Enter gender: ")
    output[OCCUPATION] = input("Enter occupation: ")
    return output

print("\nWelcome To User Management System !")
while True:
    print("\nWhat would you like to do:")
    print("1. Add an entry")
    print("2. Update an entry")
    print("3. Delete an entry")
    print("4. Search an entry")
    print("5. Display all entries")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice < 1 or choice > 6:
        print("Invalid input...please try again")
    else:
        if choice == 1:
            print("Enter details for the new entry:")
            entry = get_entry_details()
            add_entry(entry)
            print("Entry successfully created...")
        elif choice == 2:
            value = select_entry_and_value()
            if check_entry_presence(value):
                print('Enter the details of the updated entry:')
                entry = get_entry_details()
                update_entry(value, entry)
                print("Entry successfully updated...")
            else:
                print("Entry not found...")
        elif choice == 3:
            value = select_entry_and_value()
            if check_entry_presence(value):
                delete_entry(value)
                print("Entry successfully deleted...")
            else:
                print("Entry not found...")
        elif choice == 4:
            value = select_entry_and_value()
            entry = search_entry(value)
            if entry:
                display_entry(entry)
            else:
                print("Entry not found...")
        elif choice == 5:
            display_all_entries()
        elif choice == 6:
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                print('Exiting...')
                break
    print()