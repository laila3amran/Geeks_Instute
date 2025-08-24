longest = ""  # store the current longest sentence

while True:
    sentence = input("Enter the longest sentence you can without 'A' (or type quit to stop): ")

    if sentence.lower() == "quit":
        print("Game ended. Your longest sentence was:", longest)
        break

    if "a" in sentence.lower():
        print("Oops! Your sentence contains an 'A'. Try again.")
    else:
        if len(sentence) > len(longest):
            longest = sentence
            print("🎉 Congrats! New longest sentence without 'A'.")
        else:
            print("Not longer than your best. Try again!")
