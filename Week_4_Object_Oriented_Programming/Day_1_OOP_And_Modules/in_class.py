import itertools

# 1


class Dog:
    def __init__(self, breed, color):
        self.color = color
        self.breed = breed

    def __add__(self, other_dog):
        return self.breed+other_dog.color

    def __repr__(self):
        return f"{self.breed} {self.color}"

    def bark(self):
        print("whoof")


def print_dogs():
    return


if __name__ == "__main__":  # for import
    dog1 = Dog("chuwawa", "black")
    dog2 = Dog("german sheppard", "brown")
    print(dog1+dog2)
    print(dog2)
    dog2.bark()

# look test.py for build in methods

# 2 Infinite Iterators

# 2.1
result = itertools.count(start=0, step=2)

for number in result:
    # termination condition
    if number < 8:
        print(number)
    else:
        break


# Cycle: Goes through the iterable, one element at a time, but repeat takes the whole iterable each time.
# Repeat: Takes an optional times parameter that can be used as a termination condition.
# 2.2
result = itertools.cycle('12345')
counter = 0

for number in result:
    # termination condition
    if counter < 10:
        print(number)
        counter = counter + 1
    else:
        break

# 2.3
result = itertools.repeat('hello', times=2)
for word in result:
    print(word)

# 3 Finite Iterators

# 3.1
# Chain: This function accepts a variable number of iterables and loops through all of them, one by one.
list_one = ['a', 'b', 'c']
list_two = ['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)

for element in result:
    print(element)

# 3.2
# Compress: This function takes in an iterable and a selector, and returns an iterable with only those items for which the corresponding selector value is true.
names = ['Alice', 'James', 'Matt']
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)

for element in result:
    print(element)

# 3.3
# DropWhile: An iterable and a function (predefined or lambda) is passed to it. Based on the condition inside the function, dropwhile keeps on dropping values from the iterable until it encounters the first element that evaluates to false.
my_list = [0, 0, 1, 2, 0, 0]

result = itertools.dropwhile(lambda x: x == 0, my_list)

for elements in result:
    print(elements)
