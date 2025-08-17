from part1 import Game

def get_user_menu_choice():
    """Show menu and get user choice (validated, no loops)."""
    print("==== Rock Paper Scissors ====")
    print("(1) Play a new game")
    print("(2) Show scores")
    print("(q) Quit")
    choice = input(" Enter your choice: ").strip().lower()

    if choice in ["1", "2", "q"]:
        return choice
    else:
        print(" Invalid choice.")
        return None


def print_results(results):
    """Print game summary."""
    print("\n===== Game Summary =====")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("========================")
    print(" Thanks for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":  # Play game
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":  # Show scores
            print_results(results)

        elif choice == "q":  # Quit
            print_results(results)
            break


if __name__ == "__main__":
    main()
