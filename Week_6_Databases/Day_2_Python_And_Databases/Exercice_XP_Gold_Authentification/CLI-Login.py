users = {"user_1": "user_1", "user_2": "user_2", "user_3": "user_3"}
user_input = ""
logged_in = []


def menu():
    print("""*****
To login input "l"
To sign in input "s"      
For exit input "x"
*****""")
    user_input = input("Make your choice...")
    if user_input.lower() == "l":
        log_in()
    elif user_input.lower() == "s":
        sign_in()
    elif user_input.lower() == "x":
        return
    else:
        print("Wrong input")
    menu()


def log_in():
    user_name = input("Input your user name...")
    password = input("Input your password...")
    if user_name in users and password == users[user_name]:
        print(f"Hello {user_name}, you  are now logged in")
        if user_name not in logged_in:
            logged_in.append(user_name)
        return logged_in
    print("Wrong user name or password")


def sign_in():
    user_name = input("Input your user name...")
    if user_name not in users.keys():
        password = input("Input your password...")
        users[user_name] = password
        return users
    else:
        print(f"'{user_name}' already taken, select new one")


print(users)
menu()
print(users)
