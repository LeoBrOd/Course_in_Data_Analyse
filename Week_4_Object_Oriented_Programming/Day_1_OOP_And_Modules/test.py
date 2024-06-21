from in_class import Dog
from in_class import print_dogs
import math
from collections import defaultdict
from collections import Counter
from collections import deque
import collections
from collections import namedtuple
from collections import OrderedDict

# 2
print("The value of cosine is", math.cos(3))
print("The value of sine is", math.sin(3))
print("The value of tangent is", math.tan(3))
print("The value of pi is", math.pi)

# 1
dog3 = Dog("billdog", "white")
dog3.bark()

# 3
# Defaultdict is exactly like a dictionary in python. The only difference is that it does not give an exception/key error when you try to access the non-existent key.
# In the following code, even though the 4th index was not initialized, the compiler still returns a value, 0, when we try to access it.
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
print(nums['four'])

# 4
list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1, 2, 2]
answer = Counter(list)
print(answer[2])

# 5
# Deque is an optimal version of list used for inserting and removing items. It can add/remove items from either start or the end of the list.
# In the following code, z is being added at the end of the given list and g is at the start of the same list.
# initialization
list = ["a", "b", "c"]
deq = deque(list)
print(deq)

# insertion
deq.append("z")
deq.appendleft("g")
print(deq)
# removal
deq.pop()
deq.popleft()
print(deq)

# 5
# The Namedtuple() solves a very major problem in the field of computer science. Usual tuples need to remember the index of each field of a tuple object, however, namedtuple() solves this by simply returning with names for each position in the tuple.
# In the following code, an index is not required to print the name of a student rather passing an attribute is sufficient for the required output.
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('Peter', 'James', '13')
print(s1.fname)
print(s1)

# 6
# ChainMap combines a lot of dictionaries together and returns a list of dictionaries. ChainMaps basically encapsulates a lot of dictionaries into one single unit with no restriction on the number of dictionaries.
# The following program ChainMap to return two dictionaries.
dictionary1 = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'b': 4}
chain_Map = collections.ChainMap(dictionary1, dictionary2)
print(chain_Map.maps)
print(chain_Map.maps[1])

# 7
# OrderedDict is a dictionary that ensures its order is maintained. For example, if the keys are inserted in a specific order, then the order is maintained. Even if you change the value of the key later, the position will remain the same.
order = OrderedDict()
order['a'] = 1
order['b'] = 2
order['c'] = 3
print(order)

# unordered dictionary
unordered = dict()
unordered['a'] = 1
unordered['b'] = 2
unordered['c'] = 3
print("Default dictionary", unordered)
