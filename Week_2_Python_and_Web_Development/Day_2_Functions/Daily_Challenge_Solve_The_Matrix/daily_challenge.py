list_of_strrings=["7ii","Tsx","h%?","i #","sM ","$a ","#t%","^r!"]
list_of_lists=[list(string) for string in list_of_strrings]
def decoder(user_list):
    password=""
    for col in range(len(list_of_lists[0])):
        for row in range(len(list_of_lists)):
            x=list_of_lists[row][col]
            if x.isalpha():
                password+=x
            else:
                if not password.endswith(" "):
                    password+=" "
    return(password)        
print(decoder(list_of_lists))