#3
    # >>> 3 <= 3 < 9 - True
    # >>> 3 == 3 == 3 - True
    # >>> bool(0) - False
    # >>> bool(5 == "5") - False
    # >>> bool(4 == 4) == bool("4" == "4") - True
    # >>> bool(bool(None)) - False
    # x = (1 == True) 
    # y = (1 == False)
    # a = True + 4
    # b = False + 10
    # print("x is", x) - x is True
    # print("y is", y) - y is false
    # print("a:", a) - a:5
    # print("b:", b) - b:10
#4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))
#5
#can be done as a function, but I am afraid that it will be a loop
message=input("Input your message without 'a' ...").lower()
length=0
if "a" in input and len(message)>length:
    length=len(message)
    print(f"Congratulations!!! Your score is {length}.")
elif "a" in input:
    print(f"You can do better! Your score is {len(message)}. Top score is {length}")
else: print("Wrong input. You might have an a in your sentences.")