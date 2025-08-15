class Farm:
    def __init__(self, farm_name ):
        self.animals={}
        self.name=farm_name
    def add_animal(self,animal_type,count=1 ):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    def get_info(self):
        info = f"Farm Name: {self.name}\nAnimals:\n"
        for animal, count in self.animals.items():
            info += f"{animal}: {count}\n"
        return info
    def get_animal_types(self):
        return sorted(self.animals.keys())
    def get_short_info(self):
        animal_list = self.get_animal_types()
        formatted_animals = []

        for animal in animal_list:
            count = self.animals[animal]
            if count > 1:
                formatted_animals.append(animal + "s")
            else:
                formatted_animals.append(animal)

        if len(formatted_animals) > 1:
            animals_str = ", ".join(formatted_animals[:-1]) + " and " + formatted_animals[-1]
        else:
            animals_str = formatted_animals[0]

        return f"{self.name}'s farm has {animals_str}."

farm1=Farm("McDonald's Farm")
farm1.add_animal("Cow", 5)
farm1.add_animal("Chicken", 10)
farm1.add_animal("Sheep",3)
print(farm1.get_info())



