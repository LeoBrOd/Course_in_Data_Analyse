from random import shuffle
user_input=input("Input your string...")
if len(user_input)<10:
    print("string not long enough")
elif len(user_input)>10:
    print("string too long")
else: print("perfect string")
print(user_input[0])
print(user_input[-1])
for i in range(len(user_input)):
    print(user_input[:i+1])
shuffling=list(user_input)
shuffle(shuffling)
user_input=''.join(shuffling)
print(user_input)