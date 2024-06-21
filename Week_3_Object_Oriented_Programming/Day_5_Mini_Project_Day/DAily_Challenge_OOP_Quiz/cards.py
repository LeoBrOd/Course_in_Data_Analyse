import random


class Card:
    def __init__(self):
        self.suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.value = ["A", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = []

    def new_deck(self):
        for suit in self.suit:
            for value in self.value:
                self.deck.append(f"{value} {suit}")
        return self.deck


class Deck:
    def __init__(self):
        pass

    new_deck = Card().new_deck()

    def shuffle(self):
        if len(self.new_deck) == 52:
            return random.shuffle(self.new_deck)
        else:
            print("you need new deck")

    def deal(self):
        if len(self.new_deck) >= 1:
            print(self.new_deck[0])
            self.new_deck.remove(self.new_deck[0])
        else:
            print("There is no cards left in a deck. Use `Shuffle method` again")


deck = Deck()
deck.shuffle()
for i in range(53):
    deck.deal()
