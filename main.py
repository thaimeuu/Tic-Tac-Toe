import random


def draw(board):
    """
    Draw a board

    Args:
        board (list): 3 x 3 matrix
    """
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}".rjust(20, " "))
    print("-+-+-".rjust(20, " "))
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}".rjust(20, " "))
    print("-+-+-".rjust(20, " "))
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}".rjust(20, " "))
    print("")


def computer_play(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "X"
            break


def player_play(board):
    while True:
        while True:
            row = input("row: ")
            if not row.isdigit() or not (1 <= int(row) <= 3):
                print("Invalid row index")
            else:
                row = int(row) - 1
                break
        while True:
            col = input("column: ")
            if not col.isdigit() or not (1 <= int(col) <= 3):
                print("Invalid column index")
            else:
                col = int(col) - 1
                break

        if board[row][col] == " ":
            board[row][col] = "O"
            break

        print("Cell already chosen!")


def check_winner(board):
    """
    Decide who the winner is

    Args:
        board (list): 3 x 3 matrix

    Returns:
        int: 0 or 1
    """
    if (
        (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X")
        or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X")
        or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X")
        or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X")
        or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X")
        or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X")
        or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X")
        or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X")
    ):
        return 0

    elif (
        (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O")
        or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O")
        or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O")
        or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O")
        or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O")
        or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O")
        or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O")
        or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O")
    ):
        return 1


def main():
    while True:
        player = input("What is your name? ")
        if not player.isalpha():
            print("Invalid, please try again")
        else:
            break

    for round in range(3):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        counter = 0
        print("")
        print(f"Round {round+1}".center(35, "-"))
        while True:
            computer_play(board)
            counter += 1
            draw(board)
            
            winner = check_winner(board)
            if winner == 0:
                print("Computer won")
                break
            
            if counter >= 9:
                print("\nDraw")
                break

            player_play(board)
            counter += 1
            winner = check_winner(board)

            if winner == 1:
                draw(board)
                print(f"{player} won")
                break


if __name__ == "__main__":
    main()
