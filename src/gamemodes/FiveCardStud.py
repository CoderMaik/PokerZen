from functools import cmp_to_key

class FiveCardStud:
    def __init__(self, nplayers):
        self.players = []
        for i in range(nplayers):
            self.players.append(Player("Jugador " + str(i)))
        self.deck = Deck()

    def init_game(self):
        for player in self.players:
            self.deck.deal(player, 5)
            player.cards = sort_hand(player.cards)
            player.show_hand()


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

    def __gt__(self, other):
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
        self.handscore = 0
        self.highcard = None

    def __repr__(self):
        return self.name

    def show_hand(self):
        print(*self.cards, sep=", ")


def sort_hand(cards):
    return sorted(cards, key=lambda card: (card.val, card.suit), reverse=True)


def highest_hand(cards):
    """
    [8] Royal Flush:    A,K,Q,J,10 -> Same Suit
    [7] Straight Flush: Sequence 5 cards same suit
    [6] Four of a kind
    [5] Full House:     Threesome + pair
    [4] Flush:          All same suit
    [3] Straight:       Sequence
    [2] Three of a kind
    [1] Two Pairs
    [0] One Pair
    [-1] High Card
    """


def royal_flush(cards):
    return cards[0].val == 12 and straight_flush(cards)


def straight_flush(cards):
    return straight(cards) and flush(cards)


def four_of_a_kind(cards):
    if cards[0].val == cards[3].val or cards[1].val == cards[4].val:
        return cards[2]


def full_house(cards):
    return (cards[0].val == cards[2].val and cards[3].val == cards[4].val) or \
           (cards[0].val == cards[1].val and cards[2].val == cards[4].val)


def flush(cards):
    return cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit


def straight(cards):
    for i in range(len(cards) - 1):
        if cards[i].val - 1 != cards[i + 1].val:
            return False
    return True


def three_of_a_kind(cards):
    if cards[0].val == cards[2].val or cards[2].val == cards[4].val:
        return cards[2]


def two_pairs(cards):
    return cards[pair(cards)], cards[pair(cards):]


def pair(cards):
    for i in range(len(cards) - 1):
        if cards[i].val == cards[i + 1].val:
            return i + 1


def high_card(cards):
    return cards[0]
