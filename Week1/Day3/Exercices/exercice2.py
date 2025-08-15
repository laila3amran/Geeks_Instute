class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    
    def bark(self):
        print(f"{self.name} says woof!")

    def jump(self):
        x=self.height * 2
        print(f"{self.name} jumps {x} cm high!”")

    


dog1 = Dog("Buddy", 60)

dog1.bark()
dog1.jump()

davids_dog=Dog("Rex","50")
print(f" the name is {davids_dog.name} and the height is {davids_dog.height} cm ")
davids_dog.bark()
davids_dog.jump()
sarahs_dog= Dog("Teacup","20")
print(f" the name is {sarahs_dog.name} and the height is {sarahs_dog.height} cm ")
sarahs_dog.bark()
sarahs_dog.jump()


dogs=[dog1,davids_dog,sarahs_dog]
bigger_dog=dogs[0]
for dog in dogs:
    if dog.height>bigger_dog.height:
        bigger_dog=dog
print(f"the bigger one is {bigger_dog}")

