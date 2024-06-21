from game import Game


def get_user_menu_choice():
    input_text = """Menu:
    (g) - Play a new game
    (s) - Show scores
    (x) - Show scores and exit
    """
    user_input = input(f"{input_text}").lower()
    if user_input == "g":
        return "g"
    elif user_input == "s":
        return "s"
    elif user_input == "x":
        return "x"
    else:
        print("Ther is no option like this, select again")
        get_user_menu_choice()


def print_results(results):
    game_results = f"""Game results:
    You won={results["won"]} times
    You lost={results["lost"]} times
    You drew={results["drew"]} times

    Thank you for playing!
    """
    print(game_results)


def main():
    results = {"won": 0, "lost": 0, "drew": 0}
    game = Game()
    x = get_user_menu_choice()
    while x != "x":
        if x == "g":
            result = game.play()
            if result == "drew":
                results["drew"] += 1
            elif result == "won":
                results["won"] += 1
            else:
                results["lost"] += 1
            x = get_user_menu_choice()
        elif x == "s":
            print_results(results)
            x = get_user_menu_choice()
    print_results(results)


main()
