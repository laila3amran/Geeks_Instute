import random

wins = 0
losses = 0

while True:
    guess = input("Guess a number between 1 and 9 (or type 'quit' to stop): ")
    
    if guess.lower() == "quit":
        print("\nGame Over 🎮")
        print("Total Wins:", wins)
        print("Total Losses:", losses)
        break
    
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    number = random.randint(1, 9)

    if guess == number:
        print("Winner! 🎉")
        wins += 1
    else:
        print(f"Better luck next time. The number was {number}.")
        losses += 1
    print("Current Score - Wins:", wins, "Losses:", losses)