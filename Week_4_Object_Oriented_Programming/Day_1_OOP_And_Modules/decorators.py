# Class Decorators

# @Staticmethod
# A static method is a method that doesn’t get self.

class MyClass:
    @staticmethod
    def add(a, b):
        return a + b


print(MyClass.add(3, 6))

# @Classmethod
# Class methods are methods that are not bound to an object but to a class.
# Its first argument is the class itself (remember that classes are objects too).


class MyClass:
    __counter = 0

    @classmethod
    def add(cls, a):
        return cls.__counter + a


my_class_add = MyClass.add(3)
print(my_class_add)

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))

# @Property

# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name

#   def email(self):
#     return "{}.{}@gmail.com".format(self.first_name,  self.last_name )

# newClass = MyClass("John", "Doe")
# print(newClass.email())
# # >> John.Doe@gmail.com


class MyClass:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.__first_name,  self.__last_name)

    @email.setter
    def email(self, name):
        self.__first_name = name


newClass = MyClass("John", "Doe")

# print(newClass.email())
# # >> TypeError: 'str' object is not callable

print(newClass.email)
# >> John.Doe@gmail.com
newClass.email = "Sarah"
print(newClass.email)
