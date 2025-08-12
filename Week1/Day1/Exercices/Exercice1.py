#Exercice1
# name="Hello world"
# for i in range():
#     print(name)

# Exercice2
# result = pow(99,3)*8
# print(result) 

# Exercice3
# user_name= str(input("Enter your name ")) 
# name="laila"
# if user_name!=name :
#     print("You are not the right person ")
# else:
#     print("Welcome laila Zwena ")

# Exercice4
# height = float(input("Enter your height in meters:"))
# if height > 1.45:
#     print("You are tall enough to ride the roller coaster!")
# else:
#     print("You are not tall enough to ride the roller coaster.")

# Exercice5
# my_fav_numbers= {1,8,7,2,0,5,8,9,10,100,10}
# print(my_fav_numbers)
# my_fav_numbers.add(15)
# my_fav_numbers.add(20)
# print(my_fav_numbers)
# friend_fav_numbers={3,6,9,12,15}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercice6
# you can not add more integers to the tuple , it's immutable 


# Exercice7
# baskets = ["Banana", "Apples", "Oranges", "Blueberries"]  
# baskets.remove("Banana")
# baskets.pop(2)
# baskets.append("kiwi")
# baskets.insert(0,"Apples")
# print(baskets.count("Apples"))
# for basket in baskets:
#     print(basket)

# baskets.clear()

# Exercice8
sandwich_orders =["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
run_out_pastrami = "Pastrami sandwich"
while run_out_pastrami in sandwich_orders : 
    sandwich_orders.remove(run_out_pastrami)

for sandwich in sandwich_orders:
    print("Preparing the order" + sandwich)

finished_sandwiches = []

for sandwich in sandwich_orders:
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)


for sandwich in finished_sandwiches:
    print("I made your  " + sandwich)
