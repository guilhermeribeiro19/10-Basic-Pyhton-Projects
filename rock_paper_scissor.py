import random

rock = "rock"
paper = "paper"
scissor = "scissor"

choices = [rock, paper, scissor]
positive = [[paper, rock], [scissor, paper], [rock, scissor]]
negative = [[rock, paper], [paper, scissor], [scissor, rock]]

def get_computer_move():
    return random.choice(choices)

def find_winner(user_move, computer_move):
    combination = [user_move, computer_move]
    if combination in positive:
        return 1
    elif combination in negative:
        return -1
    else:
        return 0
    
print("\nWelcome to the Rock, Paper, Scissors Game!")

while True:
    choice = input("Do you want to play Rock, Paper, Scissors? (y/n)  ")

    if choice.lower() == "y":
        computer_move = get_computer_move()
        while True:
            move = input("What move do you choose: (r/p/s)  ").lower()
            print(f"The computer's move is: {computer_move}")
            if move in ['r', 'p', 's']:
                if move == 'r':
                    user_move = rock
                elif move == 'p':
                    user_move = paper
                elif move == 's':
                    user_move = scissor
                print(f"The user's move is: {user_move}")
                result = find_winner(user_move, computer_move)
                if result == 1:
                    print("\nUser Won!")
                elif result == -1:
                    print("\nComputer Won!")
                else:
                    print("\nIt's a Tie!")
                break
            else:
                print("Invalid input...please try again")
    elif choice.lower() == 'n':
        print("Exiting...")
        break
    else:
        print('Invalid input...please try again')
    print()
