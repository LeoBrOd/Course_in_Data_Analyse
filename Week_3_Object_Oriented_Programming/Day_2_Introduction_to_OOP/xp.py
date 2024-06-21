# 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


sam = Cat("Sam", 10)
shusha = Cat("Shusha", 14)
mark = Cat("Mark", 10)


def find_oldest(cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or oldest_cat.age < cat.age:
            oldest_cat = cat
    return oldest_cat


oldest = find_oldest([sam, shusha, mark])

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

# 2


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()


def find_biggect(dogs):
    biggest = None
    for dog in dogs:
        if biggest is None or biggest.height < dog.height:
            biggest = dog
    return biggest


biggest = find_biggect([sarahs_dog, davids_dog])

print(f"The biggest dog is {biggest.name}, and is {biggest.height} cm")

# 3


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# 4


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"Now you have {new_animal} in your zoo")
        else:
            print(f"Sorry, you already have {new_animal} in your zoo")

    def get_animals(self):
        if len(self.animals) <= 0:
            print("Your zoo is empty")
        else:
            print(f"You have: {", ".join((self.animals))} in your zoo")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from your zoo.")
        else:
            print(f"You dont have {animal_sold}")

    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        current_letter = None

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter != current_letter:
                current_letter = first_letter
                grouped_animals[current_letter] = []
            grouped_animals[current_letter].append(animal)

        self.animals = grouped_animals

    def get_groups(self):
        if not self.animals:
            print("The zoo has no animals yet.")
            return
        print(f"\nAnimals at {self.name} zoo grouped by first letter:")
        for letter, animals in self.animals.items():
            if len(animals) == 1:
                print(f"- {letter}: {animals[0]}")
            else:
                print(f"- {letter}:")
                for animal in animals:
                    print(f"  - {animal}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Lion")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
