# # --- Exercice 1: Car Manufacturers Analysis ---
# # Given string
# cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# # Convert to list
# car_list = cars.split(", ")
# print("There are", len(car_list), "manufacturers in the list.")

# # Print in reverse order (Z-A)
# print("Manufacturers in reverse (Z-A):", sorted(car_list, reverse=True))

# # Count names with 'o'
# count_with_o = sum(1 for c in car_list if "o" in c.lower())
# print("Manufacturers with 'o':", count_with_o)

# # Count names without 'i'
# count_without_i = sum(1 for c in car_list if "i" not in c.lower())
# print("Manufacturers without 'i':", count_without_i)

# # BONUS: Handle duplicates
# car_list_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# # Remove duplicates by converting to set, then back to list
# unique_cars = list(set(car_list_with_duplicates))

# print("Unique companies (", len(unique_cars), "):", ", ".join(unique_cars))

# # BONUS 2: Ascending order, but reverse letters of each name
# reversed_names = [c[::-1] for c in sorted(unique_cars)]
# print("Manufacturers A-Z, with names reversed:", reversed_names)




# Exercice 2 
# def get_full_name(first_name, last_name, middle_name=""):
#     # Capitalize each part properly
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     middle_name = middle_name.capitalize()

#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"

# # Examples
# print(get_full_name("john", "lee", "hooker"))   
# print(get_full_name("bruce", "lee"))            




# # Exercice 3

# # Translation table (A-Z + numbers)
# ENG_TO_MORSE = {
#     "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
#     "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
#     "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
#     "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
#     "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
#     "Z": "--..",
#     "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
#     "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
# }

# # Reverse dictionary for Morse to English
# MORSE_TO_ENG = {v: k for k, v in ENG_TO_MORSE.items()}

# # Function: English -> Morse
# def english_to_morse(text):
#     text = text.upper()
#     return " / ".join(" ".join(ENG_TO_MORSE.get(ch, "") for ch in word) for word in text.split())

# # Function: Morse -> English
# def morse_to_english(morse_text):
#     words = morse_text.split(" / ")
#     decoded_words = []
#     for word in words:
#         letters = word.split()
#         decoded = "".join(MORSE_TO_ENG.get(l, "") for l in letters)
#         decoded_words.append(decoded)
#     return " ".join(decoded_words)

# # Example usage
# msg = "Hello World"
# morse = english_to_morse(msg)
# print("English:", msg)
# print("Morse:", morse)

# decoded = morse_to_english(morse)
# print("Decoded back:", decoded)

