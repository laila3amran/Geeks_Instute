
def create_letter_index_dict(word):
   
    letter_dict = {}
    
  
    for index, letter in enumerate(word.lower()):  
        
            letter_dict[letter] = [index]
    
    return letter_dict

def display_result(word, result_dict):
    
    print(f'"{word}" ➞ {result_dict}')

def main():
    
    print("Letter Index Mapper Challenge ")
    print("This program will map each letter to its positions in your word!\n")
    
   
    word = input("Please enter a word: ").strip()
    
 
    if not word:
        print("Please enter a valid word!")
        return
    
    
    result = create_letter_index_dict(word)
    
   
    print(f"\nResult:")
    display_result(word, result)
    
  
    print(f"\nStep-by-step breakdown for '{word}':")
    for i, letter in enumerate(word.lower()):
        print(f"Position {i}: '{letter}'")


def test_examples():
  
    print("Testing with provided examples:")
    print("-" * 40)
    
    examples = ["dodo", "froggy", "grapes"]
    
    for example in examples:
        result = create_letter_index_dict(example)
        display_result(example, result)
    
    print()


test_examples()


print("Additional test cases:")
print("-" * 40)

additional_tests = [
    "hello",
    "programming", 
    "aaa",
    "abcdef",
    "mississippi"
]

for test_word in additional_tests:
    result = create_letter_index_dict(test_word)
    display_result(test_word, result)

print()


print("Detailed example with 'programming':")
print("-" * 40)
word = "programming"
result = create_letter_index_dict(word)

print(f"Word: '{word}'")
print("Letter positions:")
for i, letter in enumerate(word):
    print(f"  Index {i}: '{letter}'")

print(f"\nResulting dictionary: {result}")


print(f"\nDuplicate letters in '{word}':")
for letter, positions in result.items():
    if len(positions) > 1:
        print(f"  '{letter}' appears at positions: {positions}")

print("\n" + "="*50)
print("Ready to try with your own word!")
print("Uncomment the line below to run interactively:")
print("# main()")