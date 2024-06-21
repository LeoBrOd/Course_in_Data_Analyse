import random


class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        user_options = ["rock", "paper", "Scissors"]
        while True:
            user_item = input(
                "Make your choice (rock, paper, scissors): ").lower()
            if user_item in user_options:
                return user_item
            else:
                print("invalid input. Lets try ahain")

    def get_computer_item(self):
        computer_item = random.choice(["rock", "paper", "Scissors"])
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "drew"
        elif (user_item == "scissors" and computer_item == "paper") or (user_item == "paper" and computer_item == "rock") or (user_item == "rock" and computer_item == "scissors"):
            return "won"
        else:
            return "lost"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You chose: {user_item}\nComputer chose: {
              computer_item}\nResult: {result}")
        return result
