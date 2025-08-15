#Exercice1
class Cat:
     def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1=Cat("Whiskers", 7)
cat2=Cat("Tom", 5)
cat3=Cat("Jerry", 2)

def oldest_cat():
    oldest = cat1
    for cat in [cat1, cat2, cat3]:
        if  cat.age > oldest.age:
            oldest = cat
    return oldest
oldest = oldest_cat()
print(f"The oldest cat is {oldest.name} who is {oldest.age} years old.")

