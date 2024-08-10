# 1 Write a script that inserts an item at a defined index in a list.
from numpy.linalg import norm
users_list = [1, 2, 3]


def insert_at(users_list, item, index):
    new_list = users_list[:]
    new_list.insert(index, item)
    return (new_list)


print(insert_at(users_list, "hello", 1))

# 2 Write a script that counts the number of spaces in a string.


def spaces(string):
    spaces = 0
    for i in string:
        if i == " ":
            spaces += 1
    return (f"There`s {spaces} space(s) in a string")


print(spaces("Hello world"))

# 3 Write a script that calculates the number of upper case letters and lower case letters in a string.


def tittle_letters(string):
    upper_case = 0
    lower_case = 0
    for i in string:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
    return (f"Ther`s {upper_case} upper case and {lower_case} lower case letters in a string")


print(tittle_letters("Helllo World!!!"))

# 4 Write a function to find the sum of an array without using the built in function


def my_sum(*args):
    my_sum = 0
    for num in args:
        my_sum += num
    return my_sum


print(my_sum(1, 5, 4, 2))

# 5 Write a function to find the max number in a list


def max_number(users_list):
    max_number = 0
    for num in users_list:
        if num > max_number:
            max_number = num
    return (f"Max nuber is: {max_number}")


print(max_number([0, 1, 3, 50]))

# 6 Write a function that returns factorial of a number


def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return (f"Factorial of {num} equal {factorial}")


print(factorial(4))

# 7 Write a function that counts an element in a list (without using the count method)


def list_count(users_list, element):
    element_count = 0
    for i in users_list:
        if i == element:
            element_count += 1
    return (f"There`s {element_count} {element}`s in a list")


print(list_count(['a', 'a', 't', 'o'], 'a'))

#!8 Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
x = [1, 2, 2]
l2 = norm(x)
print(l2)

# 9 Write a function to find if an array is monotonic (sorted either ascending of descending)


def is_mono(array):
    is_ascending = all(array[i] <= array[i+1] for i in range(len(array)-1))
    is_descending = all(array[i] >= array[i+1] for i in range(len(array)-1))
    return is_descending or is_ascending


print(is_mono([7, 6, 5, 5, 2, 0]))
print(is_mono([2, 3, 3, 3]))
print(is_mono([1, 2, 0, 4]))

# 10 Write a function that prints the longest word in a list.


def longest_word(users_list):
    longest_word = ""
    for i in users_list:
        if len(i) > len(longest_word):
            longest_word = i
    return (f"Longest word in a list: {longest_word}")


print(longest_word(("Write a function that prints the longest word in a list").split(" ")))

# 11 Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


def separate_integers(users_list):
    integers = [i for i in users_list if isinstance(i, int)]
    strings = [i for i in users_list if isinstance(i, str)]
    return (f"List of strings: {strings}\nList of integers: {integers}")


print(separate_integers([1, 2, "helloo", 3, "World"]))

# 12 Write a function to check if a string is a palindrome:


def is_palindrome(my_string):
    return my_string.lower() == my_string[::-1].lower()


print(is_palindrome('radar'))

# 13 Write a function that returns the amount of words in a sentence with length > k:
sentence = 'Do or do not there is no try'
k = 2


def sum_over_k(sentence, k):
    sum_over_k = 0
    for i in sentence.split(" "):
        if len(i) > k:
            sum_over_k += 1
    return (f"Amount of words in a sentence with length > k is {sum_over_k}")


print(sum_over_k(sentence, k))

# 14 Write a function that returns the average value in a dictionary (assume the values are numeric):


def dict_avg(dictionary):
    sum_of_val = 0
    num_of_val = 0
    for i in dictionary.values():
        if isinstance(i, int):
            sum_of_val += i
            num_of_val += 1
    average = sum_of_val/num_of_val
    return (f"The average value is equal {average}")


print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))

# 15 Write a function that returns common divisors of 2 numbers:


def common_div(num_1, num_2):
    divisors = []
    div_range = 0
    if num_1 < num_2:
        div_range = num_1+1
    else:
        div_range = num_2+1
    for i in range(2, div_range):
        if num_1 % i == 0 and num_2 % i == 0:
            divisors.append(i)
    return (f"Common divisors for {num_1} and {num_2} is(are): {divisors}")


print(common_div(10, 20))

# 16 Write a function that test if a number is prime:


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(is_prime(11))

# 17 Write a function that prints elements of a list if the index and the value are even:


def weird_print(array):
    list_of_el = []
    for i, v in enumerate(array):
        if i % 2 == 0 and v % 2 == 0:
            list_of_el.append(i)
    print(list_of_el)


weird_print([1, 2, 2, 3, 4, 5])

# 18 Write a function that accepts an undefined number of keyworded arguments and return the count of different types


def type_count(**kwargs):
    types = {}
    for v in kwargs.values():
        if type(v) not in types:
            types[type(v)] = 1
        else:
            types[type(v)] += 1
    return types


print(type_count(a=1, b='string', c=1.0, d=True, e=False))

# 19 Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.


def new_split(my_string, divider=" "):
    my_list = []
    word = ""
    for i in my_string:
        if i != divider:
            word += i
        elif i == divider and word != "":
            my_list.append(word)
            word = ""
    if word != "":
        my_list.append(word)
    return (my_list)


print(new_split("hello World, you are wonderfull"))
print(new_split("hello World, you are wonderfull", ","))

# 20 Convert a string into password format.


def convert_password(my_string):
    output = ""
    for i in my_string:
        output += "*"
    return output


print(convert_password("my_string"))
