class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return (f"{self.name} is barking")

    def run_speed(self):
        speed = int(self.weight/self.age*10)
        return f"{self.name}`s speed is: {speed}"

    def fight(self, other_dog):
        self_points = self.run_speed()*self.weight
        other_dog_points = other_dog.run_speed()*other_dog.weight
        if self_points < other_dog_points:
            return (f"{other_dog.name} won!!!")
        elif self_points > other_dog_points:
            return (f"{self.name} won!!!")
        else:
            return ("No one won!!!")


mat = Dog("Mat", 5, 10)
charlie = Dog("Charlie", 3, 15)
sam = Dog("Sam", 9, 12)

if __name__ == "__main__":
    print(mat.bark())
    print(charlie.run_speed())
    print(charlie.fight(mat))
