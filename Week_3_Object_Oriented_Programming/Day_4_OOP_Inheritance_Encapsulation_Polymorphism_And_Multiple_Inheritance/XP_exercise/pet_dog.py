from dog import Dog
import random


class Petdog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        other_dog_names = [dog.name for dog in args if isinstance(dog, Petdog)]
        dog_names = ", ".join([self.name] + other_dog_names)
        print(f"{dog_names} all play together!")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs",
                  "shakes your hand", "plays dead"]
        trick = random.choice(tricks)
        if self.trained == True:
            print(f"{self.name} {trick}!")


mat = Petdog("Mat", 5, 10)
charlie = Petdog("Charlie", 3, 15)
sam = Petdog("Sam", 9, 12)

mat.train()
mat.play(charlie, sam)
mat.do_a_trick()
