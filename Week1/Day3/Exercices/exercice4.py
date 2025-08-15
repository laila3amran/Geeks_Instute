class Zoo:
    def __init__(self,zoo_name):
        self.animals=[]
        self.name=zoo_name
    def add_animal(self,new_animal):
        for animal in self.animals:
            if animal == new_animal:
                print(f"{new_animal} is already in the zoo.")
            self.animals.append(new_animal)
        
    def get_animals(self):
        return self.animals
    
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
         for letter in self.animals:
             self.animals.sort()
    
    def get_groups(self):
        groups = {}
        for animal in self.animals:
            if animal not in groups:
                groups[animal] = 1
            else:
                groups[animal] += 1
        return groups

new_york_zoo=Zoo("New York Zoo")
    
new_york_zoo.add_animal("Giraffe")
new_york_zoo.get_animals()
new_york_zoo.sell_animal("Giraffe")
new_york_zoo.sort_animals()
new_york_zoo.get_groups()

             