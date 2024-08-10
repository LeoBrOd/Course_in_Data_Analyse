# 1
class Shape:
    sides = 4  # first property
    name = "Square"  # second property

    def description(a):  # method defined
        return ("A square with 4 sides")


s1 = Shape()  # creating an object of Shape
print("Name of shape is:", (s1.name))
print("Number of sides are:", (s1.sides))
print(s1.description())

# 2


class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")


class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):
        print("I am an DOGGG !!! WOUAFFF!!")


rex = Dog('dog', 4, "Wouaf")
rex.make_sound()

# 3


class Animal():
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound


class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball):
        super().__init__(type, number_legs, sound)
        # Or : Animal.__init__(self,type, number_legs, sound)
        self.fetch_ball = fetch_ball


rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)
# >> This animal is a dog

print('This dog has', rex.number_legs, ' legs')
# >> This dog has 4 legs

print('This dog makes the sound ', rex.sound)
# >> This dog makes the sound wouaf

print('Does this dog fetchs balls ? ', rex.fetch_ball)
# >> Does this dog fetchs balls ? True

# 4
