#1
l1=[1,2,3,4]
l2=[5,6,7,8]
l1.extend(l2)
print(l1)
#2
# for i in range(1500,2501):
#     print(i*5)
#     print(i*7)
#3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_input=input("Please enter your name...")
if user_input in names:
    print(names.index(user_input))
else: print("You are not on a list")
#4
user_input_1=int(input("please enter first number"))
user_input_2=int(input("please enter second number"))
user_input_3=int(input("please enter third number"))
inputs={user_input_1,user_input_2,user_input_3}
greatest_number=0
for i in inputs:
    if i>greatest_number:
        greatest_number=i
print(f"Greatest number is: {greatest_number}")
#5
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels="aeiou"
for i in alphabet:
    if i in vowels:
        print(f"{i} is a vowel")
    else: print(f"{i} is consonant")
#6
user_input=input("Please input words using space inbettwen...")
letter=input("Please select a letter...")
words=list(user_input.lower().split(" "))
for i in words:
    if letter in i:
        print(f"In `{i}` index of `{letter}` is:{i.index(letter)}")
    else: print(f"There is no letter `{letter}` in a word `{i}`")
#7
numbers=range(1,1000001)
min_number=min(numbers)
max_number=max(numbers)
total=sum(numbers)
print(f"Max number is: {max_number}\nMin number is: {min_number}\nSum of numbers equal to {total}")
#8
user_input=input("Input your numbers using `,` sign...")
user_list=list(user_input.split(","))
user_tuple=tuple(user_input.split(","))
print(user_list, user_tuple)
#9
import random
random_number=random.randint(1,9)
users_number=""
won=0
lost=0
key="quit"
while True:
    users_number=input("Please select a number from 1 to 9...")
    if users_number=="quit": break
    elif int(users_number)==random_number:
        print("You won")
        won+=1
    else: 
        print("You lost")
        lost+=1
print(f"Total games played: {won+lost}\nGames won: {won}\nGames lost:{lost}")