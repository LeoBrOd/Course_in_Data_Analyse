# 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese (Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal = Bengal("Tom", 7)
chartreux = Chartreux("Fred", 5)
siamese = Siamese("Bella", 2)
all_cats = [bengal, chartreux, siamese]
sara_pets = Pets(all_cats)
sara_pets.walk()

# 4


class Family:
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"{kwargs["name"]}, welcome to your family !")

    def is_18(self, name):
        for member in self.members:
            if member["name"] != name:
                continue
            elif member["name"] == name and member["age"] >= 18:
                return True
            return False

    def family_presentation(self):
        print(f"{self.last_name} Family:")
        for member in self.members:
            print(",".join(f"{k}:{v}" for k, v in member.items()))


rich = Family("Rich")
rich.members.append({'name': 'Michael', 'age': 35,
                     'gender': 'Male', 'is_child': False})
rich.members.append({'name': 'Sarah', 'age': 32,
                     'gender': 'Female', 'is_child': False})
rich.born(**{'name': 'Josh', 'age': 0, 'gender': 'Male', 'is_child': True})
print(rich.is_18("Sarah"))
print(rich.is_18("Josh"))
rich.family_presentation()

# 5


class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def use_power(self, name):
        for member in self.members:
            if member["name"] != name:
                continue
            elif self.is_18(member["name"]) and member["name"] == name:
                print(f"{name}`s superpower is {member["power"]}")
            else:
                raise Exception(f"{name} is too young to use powers")

    def incredible_presentation(self):
        print("Here is our powerful family!!!")
        self.family_presentation()


incredibles = TheIncredibles("Incredibles")
incredibles.members.append({'name': 'Michael', 'age': 35, 'gender': 'Male',
                           'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'})
incredibles.members.append({'name': 'Sarah', 'age': 32, 'gender': 'Female',
                           'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'})
incredibles.incredible_presentation()
incredibles.born(**{'name': 'Jack', 'age': 0, 'gender': 'Male',
                 'is_child': True, 'power': 'unknown', 'incredible_name': 'Baby Jack'})
incredibles.incredible_presentation()
incredibles.use_power("Michael")
incredibles.use_power("Jack")
