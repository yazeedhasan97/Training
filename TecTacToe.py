# X, O
# everything is an object
import random

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

X = 'X'
O = 'O'


def convert_location_to_position(location):
    if location % 3 == 0:
        raw = location // 3 - 1
    else:
        raw = location // 3

    if location % 3 == 0:
        col = 2
    else:
        col = location % 3 - 1

    return raw, col


def draw_board(board):
    print('-' * 25)
    print(f"|\t{board[0][0]}\t|\t{board[0][1]}\t|\t{board[0][2]}\t|")
    print('-' * 25)
    print(f"|\t{board[1][0]}\t|\t{board[1][1]}\t|\t{board[1][2]}\t|")
    print('-' * 25)
    print(f"|\t{board[2][0]}\t|\t{board[2][1]}\t|\t{board[2][2]}\t|")
    print('-' * 25)


def free_locations(board):
    free = []
    for raw in board:
        for col in raw:
            # if col in range(1, 10):
            #     free.append(col)
            if isinstance(col, int):
                free.append(col)
    return free


def player_move():  # function are first class citizen, and also is an object
    free = free_locations(board)
    while True:
        location = input(f"List of free locations {free}\nEnter the location of your move: ")
        try:
            location = int(location)
        except ValueError as e:
            print(f"Location must be a valid integer.\n Please try again")
            continue

        if location not in free:
            print(f"Please chose available location.")
            continue

        break

    raw, col = convert_location_to_position(location)
    board[raw][col] = player
    draw_board(board=board)


def computer_move():  # function are first class citizen, and also is an object
    free = free_locations(board)
    location = random.choice(free) # minimax()
    raw, col = convert_location_to_position(location)
    board[raw][col] = computer
    draw_board(board=board)


def is_winner(board):
    # raw
    for i in range(len(board)):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        if board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    # diagonal
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O

    # inverse diagonal
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    # col
    for i in range(len(board)):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

    return False


def main():
    draw_board(board=board)

    if is_first:
        player_move()

    import time

    start = time.time()
    # TODO: increase the performance
    # TODO: hire recursion
    # TODO: Replace the computer random move with MiniMax Algorithm - AI
    while not is_winner(board) and free_locations(board):
        computer_move()
        if not is_winner(board) and free_locations(board):
            player_move()
    print(time.time() - start)

    winner = is_winner(board)
    if winner == X:
        print(f"PLayer with {X} is a winner")
    elif winner == O:
        print(f"PLayer with {O} is a winner")
    else:
        print("Uninformatively... its a draw!!!")


if __name__ == "__main__":  # validation
    while True:
        player = input("X or O? ").upper()
        if player not in [X, O]:
            print("Please enter a valid input ... try again")
            continue
        if player == X:
            computer = O
        else:
            computer = X

        print(f"Computer will play with {computer}")
        break

    while True:
        is_first = input("Do you want to start first? [Y/n]").upper()
        if is_first in ["Y", "YES", "YEAH"]:
            is_first = True
            print("Player will start first")
        elif is_first in ["N", "NO", "NAH"]:
            is_first = False
            print("Computer will start first")
        else:
            print("Please enter a valid input ... try again")
            continue
        break

    main()


def print_r(num):  # definition of the input
    if num == 0:  # base case
        pass
    else:
        print(num - 1)
        print_r(num - 1)  # step


def feb(num):  # definition of the input
    if num == 0:  # base case
        return 1
    elif num == 1:
        return 1
    else:
        return feb(num - 1) + feb(num - 2) # steps
