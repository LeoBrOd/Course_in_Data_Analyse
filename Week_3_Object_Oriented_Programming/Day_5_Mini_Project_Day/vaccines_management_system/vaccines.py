class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        bloodtypes = ["a", "b", "ab", "o"]
        self.id_number = id_number
        self.name = name.capitalize()
        self.age = int(age)
        self.priority = priority
        self.blood_type = blood_type
        if self.blood_type.lower() not in bloodtypes:
            raise ValueError(
                f"Wrong blood type! Please select from the list: {bloodtypes}")
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
            if person != self and person.add_family_member(self) is not self:
                person.family.append(self)
        else:
            print(f"{person.name} already in your family list")


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        self.humans.append(person)

    def find_in_queue(self, person):
        if person in self.humans:
            return self.humans.index(person)
        else:
            return f"{person.capitalize()} not in the line"

    def swap(self, person1, person2):
        if person1 in self.humans and person2 in self.humans:
            p1 = self.humans.index(person1)
            p2 = self.humans.index(person2)
            self.humans[p2], self.humans[p1] = self.humans[p1], self.humans[p2]
        else:
            print("One or two persons are missing in a list")

    def get_next(self):
        if len(self.humans) > 0:
            x = self.humans[0].name
            del self.humans[0]
            return x

        # print("There are no people in waiting list")
        None

    def get_next_blood_type(self, blood_type):
        for i in self.humans:
            if i.blood_type == blood_type.lower():
                return f"{i.name} have a `{blood_type}` blood type"
        # return f"There are no people with {blood_type} blood type in a line."
        None

    def sort_by_age(self):
        new_order = []
        for i in self.humans:
            if i.priority == True:
                new_order.append(i)
        for i in self.humans:
            if i.age >= 60 and i not in new_order:
                new_order.append(i)
        for i in self.humans:
            if i.age < 60 and i not in new_order:
                new_order.append(i)
        self.humans = new_order
        return self.humans


petr = Human(1, "Petr", 55, False, "a")
mark = Human(2, "Mark", 30, False, "o")
john = Human(3, "John", 57, True, "ab")
sofia = Human(4, "Sofia", 65, False, "b")
julia = Human(5, "Julia", 30, False, "o")

new_Queue = Queue()
new_Queue.add_person(petr)
new_Queue.add_person(mark)
new_Queue.add_person(john)
new_Queue.add_person(sofia)
new_Queue.add_person(julia)

print("Order:")
for i in new_Queue.humans:
    print(i.name)
print(new_Queue.get_next_blood_type("b"))
print(new_Queue.get_next_blood_type("a"))
print(new_Queue.find_in_queue(julia))
print(new_Queue.get_next())
print(new_Queue.get_next_blood_type("a"))
new_Queue.swap(sofia, petr)
print("Swaped order:")
for i in new_Queue.humans:
    print(i.name)
new_Queue.sort_by_age()
print("Sorted order:")
for i in new_Queue.humans:
    print(i.name)

julia.add_family_member(mark)
