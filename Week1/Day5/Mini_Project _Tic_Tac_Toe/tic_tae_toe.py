def display_board(board):
    """Display the Tic Tac Toe board in a user-friendly format."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def player_input(player, board):
    """Ask the player for their move (1-9), validate, and update board."""
    while True:
        try:
            choice = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a position (1-9): "))
            if choice < 1 or choice > 9:
                print(" Invalid input. Please select a number between 1 and 9.")
            elif board[choice - 1] != " ":
                print(" That spot is already taken. Try again.")
            else:
                board[choice - 1] = "X" if player == 1 else "O"
                break
        except ValueError:
            print(" Invalid input. Please enter a number.")


def check_win(board):
    """Check if there's a winner or tie. Return 'X', 'O', 'tie', or None."""
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] != " ":
            return board[a]  # 'X' or 'O'

    if " " not in board:
        return "tie"

    return None  # game still ongoing


def play():
    """Main function to play Tic Tac Toe."""
    board = [" "] * 9
    current_player = 1  # Player 1 starts with X
    winner = None

    print(" Welcome to Tic Tac Toe!")
    display_board([str(i+1) for i in range(9)])  # Show positions

    while winner is None:
        display_board(board)
        player_input(current_player, board)
        winner = check_win(board)
        current_player = 2 if current_player == 1 else 1  # Switch player

    display_board(board)

    if winner == "tie":
        print(" It's a tie!")
    else:
        print(f" Player {'1' if winner == 'X' else '2'} ({winner}) wins!")


# Run the game
if __name__ == "__main__":
    play()
