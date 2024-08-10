#1
print("Hello world\n"*4)
#2
a=99**3*8
print(a)
#3
    # 5 < 3 - True
    # 3 == 3 - True
    # 3 == "3" - False
    # "3" > 3 - False
    # "Hello" == "hello" - False
#4
computer_brand="Lenovo"
print(f"I have a {computer_brand} computer")
#5
name="Leonid"
age=33
shoe_size=40
info=f"Hi, my name is {name} and I am {age}.\n Guess my shoe size? Yeah, it`s {shoe_size}"
print(info)
#6
a=10
b=7
if a>b:
    print("Hello world")
#7
number=int(input("Select a number..." ))
if number%2==0:
    print("Even")
else: print("Odd")
#8
name_for_joke=input("Please write your name..")[::-1]
print(f"Your name backwards will sound - {name_for_joke}")
#9
user_height=int(input("Input your height..."))
if user_height>=145:
    print("You are tall enough to ride")
else: print("Sorry, you need to grow some to ride")