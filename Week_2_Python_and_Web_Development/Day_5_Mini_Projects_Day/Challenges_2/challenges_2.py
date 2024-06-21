#1 Draw patterns using loop
picture_1=[[0,0,1,0,0],
           [0,1,1,1,0],
           [1,1,1,1,1]]
for row in picture_1:
    for star in row:
        if star==0: print(" ",end="")
        else: print("*",end="")
    print(" ")
print("-----")
for i in range(1,6):
    print(" "*(5-i) + "*"*i)
print("-----")
for i in range(1,6):
    print("*"*i + " "*(6-i))
for i in range(1,6):
    print(" "*i + "*"*(6-i))

#2 nalyse this code before executing it. Write some commnts next to each line. 
#Write the value of each variable and their changes, and add the final output. 
#Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): #here we find indexes of all elements of the list
    minimum = i #setting min value
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]): #comparing current element to min value
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] #here we setting position of an element
print(my_list)