# #Exercice1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dict1=dict(zip(keys, values))
# print(dict1)

#Exercice2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# for key, value in family.items():
#     if value < 3:
#         print("the ticket is free")
#     if 3<value<12 :
#         print("the ticket is $10")
#     if value>12:
#         print("the ticket is $15")

# total_cost = sum(
#     0 if value < 3 else 10 if 3 < value < 12 else 15 for value in family.values()
# ) 
# print(f"Total cost of tickets: ${total_cost}")
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# family1={f"name":{user_name},f"age":{user_age}}
# print(family1)

#Exercice3
# brand={
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": ["Amancio", "Ortega", "Gaona"],
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]

# }
# }
# brand["number_stores"]=0
# print(brand)
# print(f" Zaras clients are {brand['type_of_clothes']}")
# brand["country_creation "] = "spain"
# print(brand)
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# print(brand["international_competitors"])

# del brand["creation_date"]
# print(brand["international_competitors"][2])
# print(brand["major_color"]["US"][1])
# print(f"the amount of keys are {len(brand.keys())} and values are {len(brand.values())} ")
# print(f"keys are {brand.keys()}")

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores":10000
# }

# print(f"the brand information has been updated: {brand}")

# print(f"the number of stores is now: {brand['number_stores']}")

#What just happened?"The update() method merged the 'more_on_zara' dictionary into the 'brand' dictionary Since both dictionaries had a 'number_stores' key, the value from 'more_on_zara' (10000)") overwrote the existing value in 'brand' (which was 2). The 'creation_date' key was") also added back to the dictionary with the value 1975





# Exercise 4


# def describe_city(city, country="Morocco"):
    
#     print(f"{city} is in {country}.")

# print("Calling describe_city() with different parameters:\n")
# describe_city("Reykjavik", "Iceland")
# describe_city("Casablanca")
# describe_city("Paris", "France")
# describe_city("Tokyo", "Japan")
# describe_city("Marrakech")  

# print("\nMore examples:")
# describe_city("New York", "United States")
# describe_city("Fez")  
# describe_city("London", "United Kingdom")


#exercise 5


# import random

# def number_comparison(user_number):

    
#     if not (1 <= user_number <= 100):
#         print("Please enter a number between 1 and 100.")
#         return
    
#     random_number = random.randint(1, 100)
    

#     if user_number == random_number:
#         print(" SUCCESS! You guessed the correct number!")
#         print(f"Both numbers are: {user_number}")
#     else:
#         print("FAIL! The numbers don't match.")
#         print(f"Your number: {user_number}")
#         print(f"Random number: {random_number}")

# print("Testing the number comparison function:\n")


# test_numbers = [25, 50, 75, 1, 100, 42]

# for num in test_numbers:
#     print(f"Testing with number {num}:")
#     number_comparison(num)
#     print("-" * 30)

# print("\nMultiple attempts with the same number (50) to show randomness:")
# for i in range(5):
#     print(f"Attempt {i+1}:")
#     number_comparison(50)
#     print()

# # 🌟 Exercise 6
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is '{text}'")



# make_shirt('Medium', 'Hello World')


# def make_shirt(size='Large', text='I love Python'):
#     print(f"The size of the shirt is {size} and the text is '{text}'")

# print("Modified function with default values")
# print()

# print(" Large shirt with default message")
# make_shirt()
# print()


# print(" Medium shirt with default message")
# make_shirt('Medium')
# print()


# print(" Custom size with different message")
# make_shirt('Small', 'Code like a champion!')
# print()

# print(" Bonus - Using keyword arguments")
# print()


# make_shirt(size='XL', text='Python is awesome!')
# print()


# make_shirt(text='Keep calm and code on')
# print()


# make_shirt(size='Small')
# print()


# make_shirt(text='Debugging is my superpower', size='Medium')
# print()


# print("Additional examples showing function flexibility:")
# print()

# shirts_to_make = [
#     ('XS', 'Tiny but mighty!'),
#     ('XXL', 'Big dreams, big shirt!'),
#     ('Medium', 'Just right!'),
# ]

# for size, message in shirts_to_make:
#     make_shirt(size, message)

# print()
# print("Using only defaults (no arguments):")
# make_shirt()

# Exercise 7: 

# import random


# def get_random_temp():
#     """
#     Returns a random integer between -10 and 40 degrees Celsius.
#     """
#     return random.randint(-10, 40)


# print("Step 1: Testing basic get_random_temp() function")
# print("Random temperatures:")
# for i in range(5):
#     temp = get_random_temp()
#     print(f"Test {i+1}: {temp}°C")
# print()


# def main():
#     """
#     Gets a random temperature and provides friendly advice.
#     """
#     temperature = get_random_temp()
#     print(f"The temperature right now is {temperature} degrees Celsius.")
    
    
#     if temperature < 0:
#         print("Brrr, that's freezing! Wear some extra layers today ")
#     elif 0 <= temperature <= 16:
#         print("Quite chilly! Don't forget your coat ")
#     elif 16 < temperature <= 23:
#         print("Nice and comfortable! Perfect weather for a walk ")
#     elif 24 <= temperature <= 32:
#         print("Warm and pleasant! Great day to be outside ")
#     else:  #
#         print("It's getting hot! Stay hydrated and find some shade ")

# print("Step 2-3: Basic main() function with advice")
# main()
# print()


# def get_random_temp(season):
    
#     season = season.lower()
    
#     if season == 'winter':
#         return random.randint(-10, 16)
#     elif season == 'spring':
#         return random.randint(5, 25)
#     elif season == 'summer':
#         return random.randint(20, 40)
#     elif season in ['autumn', 'fall']:
#         return random.randint(0, 20)
#     else:
#         print(f"Unknown season '{season}'. Using default range.")

# Exercise 8: Star Wars Quiz

# Quiz data
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def ask_questions(quiz_data):
   
#     correct = 0
#     incorrect = 0
#     wrong_answers = []
    
#     print("Welcome to the Star Wars Knowledge Quiz! ")
#     print("May the Force be with you!\n")
    
#     for i, item in enumerate(quiz_data, 1):
#         print(f"Question {i}: {item['question']}")
#         user_answer = input("Your answer: ").strip()
        
#         # Check if answer is correct (case-insensitive)
#         if user_answer.lower() == item['answer'].lower():
#             print(" Correct! Well done, young Padawan!\n")
#             correct += 1
#         else:
#             print(f" Incorrect. The correct answer is: {item['answer']}\n")
#             incorrect += 1
#             # Store wrong answer details for bonus feature
#             wrong_answers.append({
#                 'question': item['question'],
#                 'user_answer': user_answer,
#                 'correct_answer': item['answer']
#             })
    
#     return correct, incorrect, wrong_answers

# def display_results(correct_count, incorrect_count, total_questions):
    
#     print("=" * 50)
#     print(" QUIZ RESULTS ")
#     print("=" * 50)
    
#     print(f"Correct answers: {correct_count}")
#     print(f"Incorrect answers: {incorrect_count}")
#     print(f"Total questions: {total_questions}")
    
    
#     percentage = (correct_count / total_questions) * 100
#     print(f"Score: {percentage:.1f}%")
    
    
#     if correct_count == total_questions:
#         print("\n Perfect score! You are a true Jedi Master! ")
#         print("Your knowledge of the Force is strong!")
#     elif correct_count >= total_questions * 0.8:  
#         print("\n Excellent work! You're well on your way to becoming a Jedi Knight!")
#         print("The Force is strong with this one!")
#     elif correct_count >= total_questions * 0.6:  
#         print("\n Good job! You have solid Star Wars knowledge!")
#         print("Keep studying the ways of the Force!")
#     elif correct_count >= total_questions * 0.4:  
#         print("\n Not bad, but you could use more training, young Padawan!")
#         print("Perhaps you should rewatch the movies?")
#     else:
#         print("\n Looks like you need to brush up on your Star Wars knowledge!")
#         print("Time for a movie marathon!")

# def show_wrong_answers(wrong_answers):
    
#     if not wrong_answers:
#         return
    
#     print("\n" + "=" * 50)
#     print(" REVIEW: Questions You Got Wrong")
#     print("=" * 50)
    
#     for i, wrong in enumerate(wrong_answers, 1):
#         print(f"{i}. Question: {wrong['question']}")
#         print(f"   Your answer: {wrong['user_answer']}")
#         print(f"   Correct answer: {wrong['correct_answer']}")
#         print()

# def play_again():
    
#     while True:
#         choice = input("Would you like to play again? (yes/no): ").strip().lower()
#         if choice in ['yes', 'y']:
#             return True
#         elif choice in ['no', 'n']:
#             return False
#         else:
#             print("Please enter 'yes' or 'no'.")

# def main():
   
#     while True:
        
#         correct, incorrect, wrong_answers = ask_questions(data)
#         total = len(data)
        
       
#         display_results(correct, incorrect, total)
        
      
#         show_wrong_answers(wrong_answers)
      
#         if incorrect > 3:
#             print(f"\n You got {incorrect} questions wrong. How about another try?")
#             print("Practice makes perfect!")
            
#         if not play_again():
#             print("\n Thanks for playing the Star Wars Quiz! ")
#             print("May the Force be with you, always!")
#             break
#         else:
#             print("\n" + "="*50)
#             print(" Starting a new quiz! ")
#             print("="*50 + "\n")


# def demo_run():
    
#     print(" DEMO MODE: Star Wars Quiz ")
#     print("Showing how the quiz works with sample answers...\n")
    
   
#     demo_answers = ["Grogu", "Alderaan", "1977", "Luke Skywalker", "Darth Vader", "Ewok"]
    
#     correct = 0
#     incorrect = 0
#     wrong_answers = []
    
#     for i, item in enumerate(data):
#         print(f"Question {i+1}: {item['question']}")
#         user_answer = demo_answers[i]
#         print(f"Demo answer: {user_answer}")
        
#         if user_answer.lower() == item['answer'].lower():
#             print(" Correct!\n")
#             correct += 1
#         else:
#             print(f"Incorrect. Correct answer: {item['answer']}\n")
#             incorrect += 1
#             wrong_answers.append({
#                 'question': item['question'],
#                 'user_answer': user_answer,
#                 'correct_answer': item['answer']
#             })
    
#     display_results(correct, incorrect, len(data))
#     show_wrong_answers(wrong_answers)


# demo_run()

# print("\n" + "="*60)
# print("To play the interactive version, uncomment the line below:")
# print(" main()")

