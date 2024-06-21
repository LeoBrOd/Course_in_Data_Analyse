class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, new_animal, quantity=1):
        if new_animal in self.animals:
            self.animals[new_animal] += quantity
        else:
            self.animals[new_animal] = quantity

    def get_info(self):
        beginning = f"{self.name}'s farm\n\n"
        middle = ""
        for animal, quantity in self.animals.items():
            middle += f"{animal} : {quantity}\n"
        end = "\nE-I-E-I-O!"
        info = beginning+middle+end
        return info

    def get_animal_types(self):
        return list(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = ", ".join(
            [f"{animal}{'s' if self.animals[animal] > 1 else ''}" for animal in animal_types[:-1]])
        if len(animal_types) > 1:
            animal_list += f" and {animal_types[-1]}{
                's' if self.animals[animal_types[-1]] > 1 else ''}"
        else:
            animal_list = animal_types[0]
        return f"{self.name}'s farm has {animal_list}."


macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
