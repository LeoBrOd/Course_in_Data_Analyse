# #1
# my_age=33
# print(f"I will be:{my_age+123879}years")
# #2
# first_name="Leonid"
# last_name="Brodskyi"
# print(f"My first name is {first_name}\nMy last name is: {last_name}")
# #3
# #For example,  
# #my_name = "Frank"  this line creates a name variable type: string 
# #print("My name is {}".format(my_name))

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print("There are", cars, "cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car,"in each car.")
#4
#User first name in string starting from a capital letter
user_first_name=input("Please input your First name...").capitalize()
#User last name in string starting from a capital letter
user_last_name=input("Please input your Last name...").capitalize()
#User email in string in small letters
user_email=input("Please input your email...").lower()
#User email is an integer
user_age=int(input("Please input your age..."))
#User email in string in small letters
user_gender=input("Please input your gender...").lower()
#I`m printing everything using formating`
print(f"Hello, {user_first_name} {user_last_name}\nYou are {user_age}\nYour email is: {user_email}\nYour gender: {user_gender}")