from menu_item import MenuItem
from menu_manager import MenuManager


def show_user_menu():
    print("""Add an Item (A)
Delete an Item (D)
Update an Item (U)
Show the Menu (S)""")
    user_input = input("Please select your input")
    if user_input.lower() == "v":
        return "hello"
    elif user_input.lower() == "a":
        add_item_to_menu()
    elif user_input.lower() == "d":
        remove_item_from_menu()
    elif user_input.lower() == "u":
        update_item_from_menu()
    elif user_input.lower() == "s":
        show_restaurant_menu()
        return
    else:
        print("Wrong input.")
        show_user_menu()
    show_user_menu()


def add_item_to_menu():
    try:
        name = input("Please input item`s name")
        price = int(input("Please input item`s price"))
        item = MenuItem(name, price)
        item.save()
    except Exception as e:
        print(f"Error: Item already exists!")


def remove_item_from_menu():
    try:
        name = input("Please input item`s name")
        item = MenuManager.get_by_name(name)
        item.delete()
    except Exception as e:
        print(f"Error: There is no item like this!")


def update_item_from_menu():
    try:
        name = input("Please input item`s name")
        new_name = input("Please input new item`s name")
        new_price = int(input("Please input new item`s price"))
        item = MenuManager.get_by_name(name)
        item.update(new_name, new_price)
    except Exception as e:
        print(f"Error: Item already exists!")


def show_restaurant_menu():
    data = MenuManager.all_items()
    print(" *** Menu ***")
    for i in data:
        print(f"{i[0]} - {i[1]} NIS")


show_user_menu()
