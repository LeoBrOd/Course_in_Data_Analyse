symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    board = f"""
    {"*"*13}
    * {symbols[0]} | {symbols[1]} | {symbols[2]} *
    * - | - | - *
    * {symbols[3]} | {symbols[4]} | {symbols[5]} *
    * - | - | - *
    * {symbols[6]} | {symbols[7]} | {symbols[8]} *
    {"*"*13}
    """
    return board


def player_input(turn):
    user_input = int(input(f"player {turn}, select your cell..."))
    if user_input in symbols:
        symbols[symbols.index(user_input)] = turn
        print(display_board())
        print(turn)
    else:
        print("Cell is busy. Choose another one")
        player_input(turn)


def check_win():
    if symbols[0] == symbols[1] == symbols[2]:
        return (f"User {symbols[0]} won!!!")
    elif symbols[3] == symbols[4] == symbols[5]:
        return (f"User {symbols[3]} won!!!")
    elif symbols[6] == symbols[7] == symbols[8]:
        return (f"User {symbols[6]} won!!!")
    elif symbols[6] == symbols[3] == symbols[0]:
        return (f"User {symbols[6]} won!!!")
    elif symbols[7] == symbols[4] == symbols[1]:
        return (f"User {symbols[7]} won!!!")
    elif symbols[8] == symbols[5] == symbols[2]:
        return (f"User {symbols[8]} won!!!")
    elif symbols[6] == symbols[4] == symbols[2]:
        return (f"User {symbols[4]} won!!!")
    elif symbols[8] == symbols[4] == symbols[0]:
        return (f"User {symbols[4]} won!!!")


def play():
    print("Welcome, Players!!!")
    print(display_board())
    turn = "X"
    for i in range(len(symbols)):
        if i % 2 == 0:
            turn = "0"
        else:
            turn = "X"
        player_input(turn)
        if check_win():
            print(check_win())
            break
        elif i == len(symbols):
            print("There are no winners today")


play()
