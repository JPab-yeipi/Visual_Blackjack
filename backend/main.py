# libraries:
from deck import *
from players import *

name = input("enter your name: ")
player = Player(name)

print(f'welcome {player.name}')

croupier = Player("Croupier")
deck = Deck()

print("first hit -----------")

player.hit(deck)
croupier.hit(deck)

print(f'croupier hand: {croupier.hand[0]}, ********* -> total value: {croupier.hand_value}')
print(f'player hand: {player.hand} -> total value: {player.hand_value}')

print("---------------------------------------------------------------------")
croupier.play(deck)


