import random

from Week1.Day4.Exercices.exercice2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight) 
        self.trained = trained
    
    def train(self):
        print(self.bark())  
        self.trained = True  
    
    def play(self, *args):
        
        if args:
            dog_names = ", ".join(args)
            print(f"{dog_names} all play together")
        else:
            print(f"{self.name} plays alone")
    
    def do_a_trick(self):
        if self.trained:
            
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs", 
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet and cannot do tricks")




pet_dog1 = PetDog("Fluffy", 4, 15)
pet_dog2 = PetDog("Spot", 3, 18)
pet_dog3 = PetDog("Luna", 5, 22)



print("Before training:")
pet_dog1.do_a_trick()


print(f"\nTraining {pet_dog1.name}:")
pet_dog1.train()



print("\nAfter training:")
pet_dog1.do_a_trick()



print("\nPlay time:")
pet_dog1.play("Spot", "Luna", "Rex")
pet_dog2.play("Fluffy")



print(f"\nTraining {pet_dog2.name} and {pet_dog3.name}:")
pet_dog2.train()
pet_dog3.train()

print("\nTrick demonstration:")
pet_dog1.do_a_trick()
pet_dog2.do_a_trick()
pet_dog3.do_a_trick()