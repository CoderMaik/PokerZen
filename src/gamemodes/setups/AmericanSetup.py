"""
File contains objects used in the dem: Card, deck and player to add modularity
access to the attributes is not restricted, they are all public
"""


class Card(object):
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        # This could be done with pattern matching from python 3.10
        values = {
            0: "2",
            1: "3",
            2: "4",
            3: "5",
            4: "6",
            5: "7",
            6: "8",
            7: "9",
            8: "10",
            9: "J",
            10: "Q",
            11: "K",
            12: "A"
        }
        suits = {
            0: "\u2663",  # Clubs
            1: "\u2666",  # Diamonds
            2: "\u2665",  # Hearts
            3: "\u2660"  # Spades
        }
        return values[self.val] + suits[self.suit]

    def __gt__(self, other):
        # Overriding this method allows for instant comparison between cards
        if self.val == other.val:
            return self.suit > other.suit
        return self.val > other.val


class Deck(set):
    # Using a set helps us avoid the shuffle action, since you can only pop elements randomly
    def __init__(self):
        super().__init__()
        [[self.add(Card(i, j)) for j in list(range(4))] for i in list(range(13))]

    def deal(self, target, number=1):
        for i in range(number):
            target.cards.append(self.pop())


class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.cards = []

    def __repr__(self):
        return self.name

    def show_hand(self):
        # Pythonic way of printing the hand
        print(*self.cards, sep=", ")
