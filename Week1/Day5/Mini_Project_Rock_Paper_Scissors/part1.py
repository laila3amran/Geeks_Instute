import random

class Game:
    def get_user_item(self):
        """Ask the user to select rock/paper/scissors (with validation)."""
        while True:
            choice = input("Select (rock/paper/scissors): ").strip().lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            print(" Invalid choice. Please try again.")

    def get_computer_item(self):
        """Randomly select rock/paper/scissors for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Determine the result (win, draw, loss)."""
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        """Play one round of Rock-Paper-Scissors."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # Print outcome
        print(f"\n You selected {user_item}. Computer selected {computer_item}.")
        if result == "win":
            print(" You win!\n")
        elif result == "loss":
            print("  You lose!\n")
        else:
            print(" It's a draw!\n")

        return result
