#1
def display_message():
    print("We are learning functions now!")
display_message()
#2
def favorite_book(title):
    print(F"One of my favorite books is {title}")
#3
def describe_city(city,country="Ukraine"):
    print(f"{city} is in {country}")
describe_city("Odessa")
describe_city("New York","Usa")
#4
import random
def guess_number():
    number=int(input("select a number from 1 to 100"))
    random_number=random.randint(1,100)
    if number==random_number:
        print ("You won")
    else: print("You lost")
guess_number()
#5
def make_shirt(size="Large",text="I love Python"):
    return(f"The size of the shirt is {size} and the text is {text}")
print(make_shirt())
print(make_shirt("medium"))
print(make_shirt("Small","something new"))
print(make_shirt(text="world",size="Hello"))
#6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(users_list):
    for i in users_list:
        print(i)
def make_great(names):
    for i in range(len(names)):
        names[i]="The Great " +names[i]
make_great(magician_names)
show_magicians(magician_names)