#1
my_fav_numbers={13,19,18,7,1991,22}
my_fav_numbers.add(33)
my_fav_numbers.add(55)
my_fav_numbers.remove(55) # we can`t really remove last number cause it`s unordered
friend_fav_numbers={1,2,3,4,5,6,7}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print("Result:",our_fav_numbers)
#2
#Tuples are unchangeable
#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(0)
basket.pop()
basket.append("Kiwi")
basket.insert(0,"Apples")
basket.count("Apples")
basket=[]
print("Basket:",basket)
#4
numbers=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
numbers_second_way=[]
for i in range(3,11):
    numbers_second_way.append(i/2)
print("Another way:",numbers_second_way)
#5
for num in range (1,21):
    print(num)
for num in range (1,21):
    if num%2==0:
        print(num)
#6
name="Leonid"
user_input=""
while user_input!=name:
    user_input=input("Input your name...")
print(f"Hello, {name}")
7
list_input=input("Please write your favorite fructs using space").lower()
users_list=list(list_input.split(" "))
user_input=input("Please select a fruit").lower()
if user_input in users_list:
    print("You chose one of your favorite fruits! Enjoy!")
else: print("You chose a new fruit. I hope you enjoy")
#8
key="quit"
toppings=set()
user_input=""
while key!=user_input:
    user_input=input("Please select your topping...")
    if user_input==key: break
    toppings.add(user_input)
    print(f"You will add {user_input} to your pizza")
list_of_toppins=list(toppings)
for i in list_of_toppins:
    print(i)
price_of_pizza=10+2.5*len(list_of_toppins)
print(price_of_pizza)
#9 part 1
order=input("Please write your ages using space")
sum_of_order=0
users_age=[int(i) for i in order.split(" ")]
for i in users_age:
    if i>3 and i<=12:
        sum_of_order+=10
    elif i>12:
        sum_of_order+=15
print(f"Sum of your order: {sum_of_order} NIS")
#9 part 2
key="quit"
guest_input=[]
guest_list=[]
while True:
    guest_input=list(input("Please write your name and age using ',' sign" ).split(","))
    if guest_input==[key]: break
    elif int(guest_input[1]) in range(16,22):
        guest_list.append(guest_input)
print(f"Permited to enter: {guest_list}")
#10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
print(f"Finished sandwiches: {finished_sandwiches}")