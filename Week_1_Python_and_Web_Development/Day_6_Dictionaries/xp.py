#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict=dict(zip(keys,values))
print(new_dict)
#2
family = {}
name=""
age=0
total=0
while True:
    name=input("Enter your name or `done` to finish")
    if name=="done": break
    age=int(input("Enter your age"))
    family[name]=age
for name,age in family.items():
    if age<=3:
        cost=0
        print(f"{name} doesn`t have to pay")
    elif age>3 and age<=12:
        cost=10
        print(f"{name} has to pay: {cost} NIS")
        total+=cost
    else: 
        cost=15
        print(f"{name} has to pay: {cost} NIS")
        total+=cost
print(f"The family's total cost for the movies is: {total} NIS")
#3
brand={
    "name": "Zara", 
    "creation_date": 1975, 
    "creator_name": ["Amancio", "Ortega", "Gaona"], 
    "type_of_clothes": ['men', "women", "children", "home"], 
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000, 
    "major_color": 
        {"France": "blue", 
         "Spain": "red", 
         "US": ["pink", "green"]
     }}
brand["number_stores"]=2
