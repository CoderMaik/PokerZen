from gamemodes.setups.AmericanSetup import *


class FiveCardStud:
    def __init__(self, nplayers):
        # Initializing players and deck each round
        self.players = []
        for i in range(nplayers):
            self.players.append(Player("Player " + str(i + 1)))
        self.deck = Deck()

    def init_game(self):
        # We use dictionary to substitute switch_case
        scores = {
            8: "Royal flush",
            7: "Straight flush",
            6: "Four of a kind",
            5: "Full house",
            4: "Flush",
            3: "Straight",
            2: "Three of a kind",
            1: "Two pairs",
            0: "Pair",
            -1: "Highest card"
        }
        for player in self.players:
            # Deals 5 cards to each player and then sorts it in descending order
            self.deck.deal(player, 5)
            player.cards = sort_hand(player.cards)
            print(player)
            player.show_hand()

        # Checks for winner or draw
        winner, score, _ = check_winner(self.players)
        if winner is not None:
            print(winner.__repr__() + " has won this round with " + scores[score])


def sort_hand(cards):
    # Sorts cards in descending order
    return sorted(cards, key=lambda card: (card.val, card.suit), reverse=True)


def check_winner(players):
    # Takes first player's hand and starts comparing its score with the rest of the table
    for i in range(len(players) - 1):
        if i == 0:
            score, rest = hand_score(players[0].cards)
            winner = players[i]
        else:
            winner, score, rest = compare_scores(winner, score, rest, players[i + 1])
            if winner is None:
                return None, None, None
    return winner, score, rest


def compare_scores(winner, score, rest, player2):
    """
    We keep our current winner, its score, and the "rest" which is a card used in case
    two players have the same combination of cards (for example, two players with a pair)
    and require to compare them in order to check the best hand.

    Since this is a demo, I haven't implemented yet the most detailed comparison system,
    which in case of the previous example, it would be required to check the winner between
    two players with two pairs with the same value
    """
    score2, rest2 = hand_score(player2.cards)
    if score == score2 and rest is None or rest2 is None:
        print("It looks like " + winner.__repr__() + " and " + player2.__repr__() + " have split the pot")
        return None, None, None
    if score > score2 or (score == score2 and rest > rest2):
        return winner, score, rest
    elif score < score2 or (score == score2 and rest < rest2):
        return player2, score2, rest2
    else:
        ValueError("Unable to identify winner, drawish hands")


def hand_score(cards):
    """
    To build an efficient demo, hands are only checked once, and every
    piece of information required to look for tie-breakers is returned
    with the score of the hand itself

    More detailed comparison systems would require additional return values
    or another approach, though this is the most efficient for a demo like this
    since you iterate only once and you stop when you have found the highest
    score possible, ranked below.
    """

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
        # Returns condition for royal flush and booleans from straight and flush
        return cards[0].val == 12, straight_flush(cards)

    def straight_flush(cards):
        return straight(cards), flush(cards)

    def four_of_a_kind(cards):
        # Since our hand is sorted, if cards 1-4 or 2-5 are the same, they all are
        # Returns one of the cards as tie-breaker
        if cards[0].val == cards[3].val or cards[1].val == cards[4].val:
            return cards[2]

    def full_house(cards):
        # Same strategy as four of a kind, always returns card of the three_of_a_kind as tie-breaker
        if cards[0].val == cards[2].val and cards[3].val == cards[4].val:
            return cards[1], cards[3]
        if cards[0].val == cards[1].val and cards[2].val == cards[4].val:
            return cards[3], cards[1]
        else:
            return None, None

    def flush(cards):
        # All cards must have same suit
        return cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit

    def straight(cards):
        # All cards most be consecutive
        for i in range(len(cards) - 1):
            if cards[i].val - 1 != cards[i + 1].val:
                return False
        return True

    def three_of_a_kind(cards):
        # Same strategy as four_of_a_kind
        if cards[0].val == cards[2].val or cards[2].val == cards[4].val:
            return cards[2]

    def two_pairs(cards):
        # Returns -1-1 if there are not two pairs, returns them otherwise
        pair1 = pair(cards)
        if pair1 is not None:
            pair2 = pair(cards[pair1:])
            if pair2 is not None:
                return cards[pair1], cards[pair2]
        return -1, -1

    def pair(cards):
        """
        Returns the index of the right card of the pair, used
        to check for other pairs in the two_pairs check
        """
        for i in range(len(cards) - 1):
            if cards[i].val == cards[i + 1].val:
                return i + 1
        return None

    def high_card(cards):
        # Highest card will always be the first, since we sorted them before
        return cards[0]

    """
    Starts checking for the top ranked score possible in descending order
    to avoid unnecessary iterations, returns score and second argument as tie breaker
    """

    (royal, (straight, flush)) = royal_flush(cards)
    if royal and straight and flush:
        return 8, None
    elif straight and flush:
        return 7, None
    else:
        four = four_of_a_kind(cards)
        if four is not None:
            return 6, four
        else:
            x, y = full_house(cards)
            if x is not None and y is not None:
                return 5, x
            elif flush:
                return 4, None
            elif straight:
                return 3, None
            else:
                three = three_of_a_kind(cards)
                if three is not None:
                    return 2, three
                else:
                    v, w = two_pairs(cards)
                    if v != -1 and w != -1:
                        return 1, max(v, w)
                    else:
                        pair = pair(cards)
                        if pair is not None:
                            return 0, cards[pair]
    return -1, high_card(cards)
