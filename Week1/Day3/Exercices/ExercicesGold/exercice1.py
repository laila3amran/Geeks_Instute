# import math

# class Circle:
#     def __init__(self, radius=1.0):
#         self.radius = radius

#     def perimeter(self):
#         return 2 * math.pi * self.radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def definition(self):
#         print("A circle is a shape with all points equidistant from the center.")

# # Example usage
# c = Circle(3)
# print("Perimeter:", round(c.perimeter(), 2))
# print("Area:", round(c.area(), 2))
# c.definition()



#Exercice2
# import random

# class MyList:
#     def __init__(self, letters):
#         self.letters = letters

#     def reversed_list(self):
#         return self.letters[::-1]

#     def sorted_list(self):
#         return sorted(self.letters)

#     def random_list(self):
#         # Bonus: Generate random numbers with same length
#         return [random.randint(1, 100) for _ in self.letters]

# # Example usage
# ml = MyList(['d', 'a', 'c', 'b'])
# print("Original:", ml.letters)
# print("Reversed:", ml.reversed_list())
# print("Sorted:", ml.sorted_list())
# print("Random numbers:", ml.random_list())


# exercice3

# class MenuManager:
#     def __init__(self):
#         self.menu = [
#             {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
#             {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
#             {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
#             {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
#             {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
#         ]

#     def add_item(self, name, price, spice, gluten):
#         new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
#         self.menu.append(new_dish)
#         print(f"{name} added to the menu.")

#     def update_item(self, name, price, spice, gluten):
#         for dish in self.menu:
#             if dish["name"].lower() == name.lower():
#                 dish.update({"price": price, "spice": spice, "gluten": gluten})
#                 print(f"{name} updated successfully.")
#                 return
#         print(f"{name} not found in the menu.")

#     def remove_item(self, name):
#         for dish in self.menu:
#             if dish["name"].lower() == name.lower():
#                 self.menu.remove(dish)
#                 print(f"{name} removed. Updated menu:")
#                 for d in self.menu:
#                     print(d)
#                 return
#         print(f"{name} not found in the menu.")

# # Example usage
# if __name__ == "__main__":
#     manager = MenuManager()
#     manager.add_item("Pizza", 20, "A", True)
#     manager.update_item("Salad", 20, "C", False)
#     manager.remove_item("Soup")
#     manager.remove_item("Steak")  # dish not in menu
