import argparse
from gamemodes.FiveCardStud import *

"""
Poker app demo, implemented as part of the selection process at ZenZorrito (BadgerMaps)
can be run from terminal using arguments --gamemode and --players.

If another gamemode was required
"""


def welcome_msg():
    print("------- W  E  L  C  O  M  E      T  O... -------")
    print("-----------  P  O  K  E  R  Z  E  N  ---------\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Poker dealing app for ZenZorrito Selection Team')
    parser.add_argument('--gamemode', type=str, nargs="?", default="5cardstud", help='Card game name')
    parser.add_argument('--players', type=int, nargs="?", default="4", help='Number of players')

    args = parser.parse_args()
    players = vars(args)['players']
    if not 2 <= players <= 10:
        raise ValueError("Wrong number of players: Must be 2-10")

    welcome_msg()

    # loop for different rounds
    cont = 1
    while cont != -1:
        print("/////////// R   O   U   N   D     "+str(cont)+" ///////////")

        # Allows for new gamemodes as specified in the instructions
        if vars(args)['gamemode'] == '5cardstud':
            gamemode = FiveCardStud(players)

        gamemode.init_game()
        print("Would you like to start another round? y/n")
        answer = input()
        if answer == 'n' or answer == 'N':
            cont = -1
        else:
            cont += 1
    print("Thanks for playing!\n Powered by ZenZorrito and Miguel Villar")
