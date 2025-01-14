#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.

    Parameters:
    board (list): A 3x3 list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """
    Checks if the game is a draw (no empty spaces left).

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    bool: True if the board is full and there is no winner, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    """
    # Initialize the board
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            # Get user input
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate input
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            # Check if the cell is empty
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place the player's mark
            board[row][col] = player

            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check for a draw
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter valid numbers (0, 1, or 2).")

if __name__ == "__main__":
    tic_tac_toe()
