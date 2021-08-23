# PokerZen
Poker non GUI app for ZenZorrito application

Arguments:
  --gamemode : selects package with rules and scoring system
  --players : selects the number of players (2-10), default = 4
  
How does it work:
  Players and gamemode are initialized, cards are dealt and then the comparison begins.
  Player by player, their hands are compared looking for the top ranked combination of cards possible if one 
  is found, the rest is discarded and score and tie-breakers are kept in order to be used as comparing tools 
  with other player's hands. Multiple rounds can be played in the same table.
  
  There is no bidding system nor chips and stored information since it was not required for the selection process
  
Dir tree:
  /src
    main.py
    /gamemodes
      FiveCardStud.py
      /setups
        AmericanSetup.py

/gamemodes contains the game itself, allows for future implementation of other card games
/setups may be used in the future to add spanish decks or others.

For more information, contact me on mastermaik.contact@gmail.com
 I hope you enjoy it!
 
 Codermaik
