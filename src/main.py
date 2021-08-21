import argparse
from gamemodes import FiveCardStud

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Poker dealing app for ZenZorrito Selection Team')
    parser.add_argument('--gamemode', type=str, nargs="?", default="5cardstud", help='Card game name')
    parser.add_argument('--players', type=int, nargs="?", default="2", help='Number of players')

    args = parser.parse_args()

    if vars(args)['gamemode'] == '5cardstud':
        gamemode = FiveCardStud()

# Creating our classes:
class Card(object):
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __repr__(self):
        # This could be done with pattern matching from python 3.10
        values = {
            0: '2',
            1: '3',
            2: '4',
            3: '5',
            4: '6',
            5: '7',
            6: '8',
            7: '9',
            8: '10',
            9: 'J',
            10: 'Q',
            11: 'K',
            12: 'A'
        }
        suits = {
            0: '\u2663',  # Clubs
            1: '\u2666',  # Diamonds
            2: '\u2665',  # Hearts
            3: '\u2660'  # Spades
        }
        return values[self.val] + suits[self.suit]


class Deck(set):
    # Using a set helps us avoid the shuffle action, since you can only pop elements randomly
    def __init__(self):
        super().__init__()
        [[self.add(Card(i, j)) for j in list(range(4))] for i in list(range(13))]

    def deal(self, target, number=1):
        for i in range(number):
            target.cards.add(self.pop())


class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.cards = []
        self.hand = 0
        self.highcard = None

    def __repr__(self):
        return self.name