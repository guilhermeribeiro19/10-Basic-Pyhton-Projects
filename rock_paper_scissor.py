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

    if choice == "y":
        computer_move = get_computer_move()
        while 1:
            move = input("What move do you choose: (r/p/s)  ").lower()
            print(f"The computers move is: {computer_move}")
            if "r" in move or "p" in move or "s" in move:
                if 'r' in move:
                    user_move = rock
                elif 'p' in move:
                    user_move = paper
                elif 's' in move:
                    user_move = scissor
                print(f"The users move is: {user_move}")
                if find_winner(user_move, computer_move) == 1:
                    print("\nUser Won !")
                elif find_winner(user_move, computer_move) == -1:
                    print("\nComputer Won !")
                else:
                    print("\nIt's a Tie !")
                break
            else:
                print("Invalid input...please try again")
    elif 'n' in choice.lower():
        print("Exiting...")
        break
    else:
        print('Invalid input...please try again')
    print()

