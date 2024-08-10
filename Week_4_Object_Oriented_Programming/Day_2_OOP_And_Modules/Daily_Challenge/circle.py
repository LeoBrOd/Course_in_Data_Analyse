import math
import turtle
import gc
pen = turtle.Turtle()


class Circle:
    def __init__(self, value, type):
        if type.lower() == "radius":
            self.radius = value
        elif type.lower() == "diametr":
            self.radius = value/2
        self.area = math.pi*self.radius**2

    def __repr__(self):
        return (f"Radius={self.radius}\nArea={self.area}")

    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only add Circle objects.")
        sum_of_areas = self.area+other.area
        new_radius = math.sqrt(sum_of_areas/math.pi)
        return Circle(new_radius, "radius")

    def __gt__(self, other):
        return self.area > other.area

    def __eq__(self, other):
        return self.area == other.area

    def drawing(self):
        pen.circle(self.radius)

    @classmethod
    def sorted_list(cls):
        list = []
        for i in gc.get_objects():
            if isinstance(i, cls):
                list.append(i)
        return sorted(list)


c1 = Circle(15, "radius")
c2 = Circle(20, "diametr")
print("Circle #1", c1)
print("Circle #2", c2)
c3 = c1 + c2
print("Circle #3", c3)
print("Circle #3>Circle #1", c3 > c1)
print("Circle #3=Circle #1", c3 == c1)
sorted_instances = (Circle.sorted_list())
for i in sorted_instances:
    i.drawing()
turtle.done()
