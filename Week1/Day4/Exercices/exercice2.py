class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
       
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif other_power > self_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"





dog1 = Dog("Rex", 3, 25)
dog2 = Dog("Buddy", 5, 30)
dog3 = Dog("Max", 2, 20)



print("Barking:")
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())



print(f"\nRun speeds:")
print(f"{dog1.name}'s run speed: {dog1.run_speed():.2f}")
print(f"{dog2.name}'s run speed: {dog2.run_speed():.2f}")
print(f"{dog3.name}'s run speed: {dog3.run_speed():.2f}")


print(f"\nFight results:")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))

print("\n" + "="*50 + "\n")