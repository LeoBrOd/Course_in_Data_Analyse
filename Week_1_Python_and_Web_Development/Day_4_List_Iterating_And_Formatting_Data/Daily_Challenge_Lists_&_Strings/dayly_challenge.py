#1
user_number=int(input("Input your number..."))
length_of_list=int(input("Input length..."))
output=[]
for step in range(1,length_of_list+1):
    output.append(user_number*step)
print(output)
#2
user_input=input("Input your word")
output=user_input[0]
for i in user_input:
    if i not in output:
        output+=i
print(output)