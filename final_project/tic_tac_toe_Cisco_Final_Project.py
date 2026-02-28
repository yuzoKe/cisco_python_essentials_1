from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|", end="")
        for cell in row:
            print(f"   {cell}   |", end="")
        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid move. Enter a number from 1 to 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("That square is already occupied. Try again.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Enter an integer.")


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if all(board[i][col] == sign for col in range(3)):
            return True
        if all(board[row][i] == sign for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


# ── Main game ──────────────────────────────────────────────
board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# Computer's first move: always the center
board[1][1] = 'X'
display_board(board)

while True:
    # --- User's turn ---
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    # --- Computer's turn ---
    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("I won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
