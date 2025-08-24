# #Exercice1&2
# # Dictionary with some birthdays
# birthdays = {
#     "Alice": "1995/06/12",
#     "Bob": "1988/03/24",
#     "Charlie": "2000/11/05",
#     "Diana": "1992/09/17",
#     "Ethan": "1985/01/30"
# }

# print(" Welcome! You can look up the birthdays of the people in the list!")

# # Show all names (Exercise 2)
# print("Here are the people you can choose from:")
# for name in birthdays.keys():
#     print("-", name)

# # Ask user for input
# person = input("\nWhose birthday do you want to look up? ")

# # Check if name exists
# if person in birthdays:
#     print(f"{person}'s birthday is on {birthdays[person]} ")
# else:
#     print(f"Sorry, we don’t have the birthday information for {person}.")



#Exercice3
# def special_sum(x: int) -> int:
#     # Convert x to string so we can build "XX", "XXX", etc.
#     term1 = int(str(x))
#     term2 = int(str(x) * 2)   # XX
#     term3 = int(str(x) * 3)   # XXX
#     term4 = int(str(x) * 4)   # XXXX

#     return term1 + term2 + term3 + term4

# # Example
# print("Result for X=3:", special_sum(3))  # should print 3702




#Exercice 4
# import random

# # Function to throw one dice
# def throw_dice():
#     return random.randint(1, 6)

# # Function to keep rolling until doubles appear
# def throw_until_doubles():
#     throws = 0
#     while True:
#         d1, d2 = throw_dice(), throw_dice()
#         throws += 1
#         if d1 == d2:
#             break
#     return throws

# # Main function
# def main():
#     results = []  # store all results

#     for _ in range(100):
#         throws_needed = throw_until_doubles()
#         results.append(throws_needed)

#     total_throws = sum(results)
#     average = total_throws / len(results)

#     print("\n Dice Simulation Results ")
#     print("Total throws:", total_throws)
#     print("Average throws to reach doubles:", round(average, 2))





