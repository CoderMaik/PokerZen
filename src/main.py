import argparse
from gamemodes.FiveCardStud import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Poker dealing app for ZenZorrito Selection Team')
    parser.add_argument('--gamemode', type=str, nargs="?", default="5cardstud", help='Card game name')
    parser.add_argument('--players', type=int, nargs="?", default="4", help='Number of players')

    args = parser.parse_args()
    players = vars(args)['players']
    if not 2 <= players <= 10:
        raise ValueError("Wrong number of players: Must be 2-10")

    if vars(args)['gamemode'] == '5cardstud':
        gamemode = FiveCardStud(players)
    gamemode.init_game()
