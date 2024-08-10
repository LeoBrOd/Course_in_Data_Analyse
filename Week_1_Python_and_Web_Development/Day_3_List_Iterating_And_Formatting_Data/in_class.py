#1
list1 = [5, 10, 15, 20, 25, 50, 20]
if list1.index(20):
    list1[list1.index(20)]=200
print(list1)
#2
a_tuple = (10, 20, 30, 40)
a,b,c,d=a_tuple
print(a,b,c,d)
#3
x=[1,2,3,4,5,9,8,7,3,25]
y=x[: : 2]
print(y)
z=x[: : -1]
print(z)
#4
my_list=[1,2,5,9,35,50,-2,-10,-55,25]
max=0
min=0
for i in my_list:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"Max - {max}\nMin - {min}")
#5
user_input=int(input("Input your number..."))
for i in range(1,11):
    print(f"{user_input} X {i} = {i*user_input}")
#6
counter=0
while True:
    counter+=1
    if counter >99:
        break
    if counter%2==0:
        continue
    print(counter)
#7
# # Question: Write a program that takes a list of strings and finds all the palindromes in the list.
# # A palindrome is a word that reads the same backward as forward. Print each palindrome found in the list.
# # Answer without using list comprehensions:
strings = ["level", "world", "madam", "python", "racecar", "hello", "civic"]
for i in strings:
    if i==i[::-1]:
        print(strings[i])