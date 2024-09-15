position_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

X = 'X'
O = 'O'

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def update_board(character, position):
    row, column = position_map[position]
    board[row][column] = character

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    
    return False

def check_position(position):
    row, column = position_map[position]
    if board[row][column] == X or board[row][column] == O:
        return False
    return True

print("\nWelcome to the Tic-Tac-Toe Game!")
counter = 0

while True:
    display_board()
    if counter % 2 == 0:
        while True:
            choice = int(input(f"Player {(counter%2)+1}, enter your position ('{X}'): "))
            if choice < 1 or choice > 9:
                print('Invalid input...please try again.')
            elif check_position(choice):
                update_board(X, choice)
                if check_win():
                    display_board()
                    print(f"Congratulations !!! Player {(counter%2)+1} won !!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position.")
    else:
        while True:
            choice = int(input(f"Player {(counter%2)+1}, enter your position ('{O}'): "))
            if choice < 1 or choice > 9:
                print('Invalid input...please try again.')
            elif check_position(choice):
                update_board(O, choice)
                if check_win():
                    display_board()
                    print(f"Congratulations !!! Player {(counter%2)+1} won !!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position.")
    
    if counter == 9:
        display_board()
        print("The match ended with a draw !!! Better luck next time")
        exit(0)
    print()
