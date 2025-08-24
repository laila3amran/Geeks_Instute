names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter a name: ")

if user_name in names:
    print("The first occurrence is at index:", names.index(user_name))
else:
    print("Name not found in the list.")
