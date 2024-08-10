#1
print("Htllo world\n"*4+"I love python\n"*4)
#2
choice=int(input("Please select a month..."))
if choice in [3,4,5]:
    print("Spring")
elif choice in [6,7,8]:
    print("Summer")
elif choice in [9,10,11]:
    print("Autumn")
elif choice in [12,1,2]:
    print("Winter")
else: print("Wrong input")