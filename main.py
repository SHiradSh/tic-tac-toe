def print_board(board):
    """This function prints the current board state."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the current player has won."""
    # Check rows, columns and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    """Check if the board is full."""
    return all([spot != " " for row in board for spot in row])

def tic_tac_toe():
    """Main game function."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn!")

        # Get player input
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("This spot is taken! Choose another one.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 2.")

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} Wins!!!")
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!!!")
            break

        turn += 1

# Run the game
tic_tac_toe()
