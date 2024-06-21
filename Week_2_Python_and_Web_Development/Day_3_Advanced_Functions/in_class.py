#1
numbers=[1,2,3,4,5]
even_numbers=filter(lambda x: x%2==0, numbers)
print(list(even_numbers))
#2
points=[(1,2),(3,1),(5,4),(2,7)]
sorted_points=sorted(points, key=lambda x:x[1])
print(sorted_points)
#3
try:
    x=5/0
except ZeroDivisionError: 
    print("You divided by 0")
#4
try:
    x=[1,2,3]
    x[3]=10
except: 
    print("You divided by 0")
#5
try:
    number=int("hello")
    x=5/0
except (ZeroDivisionError,ValueError) as e: 
    print(f"An error occured: {e}")
#6
def check(a,b,c):
    print(a,b,c)
a=[1,2,3]
check(*a)
#7 
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_names=filter(lambda name: len(name)<=4, people)
greetings=map(lambda name:f"Hello, {name}!", filtered_names)
print(list(greetings))
#8 not done
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
#9
books = [
    {"title": "Book A", "author": "Author X", "year_published": 2001},
    {"title": "Book B", "author": "Author Y", "year_published": 1999},
    {"title": "Book B", "author": "Author Z", "year_published": 1998}
]
sorted_books=sorted(books,key=lambda i: (i["title"],i["year_published"]))
print(sorted_books)