from DB_Connect import DbConnection
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
    query = f"select user_name, password from users where user_name='{
        user_name}' and password='{password}'"
    res = DbConnection.execute_select(query)
    if len(res) > 0:
        print(f"Hello {user_name}, you  are now logged in")
        if user_name not in logged_in:
            logged_in.append(user_name)
        return logged_in
    print("Wrong user name or password")


def sign_in():
    user_name = input("Input your user name...")
    password = input("Input your password...")
    query = f"INSERT INTO users (user_name, password) VALUES (%s,%s)"
    print(query)
    DbConnection.execute_change(query, (user_name, password))


menu()
