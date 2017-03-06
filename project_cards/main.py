'''Cards and the Player'''
#!/usr/bin/env python3
#encoding: UTF-8

import CardGame

RANK = '23456789TJQKA'
SUIT = ['spades', 'clubs', 'diamonds', 'hearts']

def main():
    print("Let's play a game!")
    main_deck = CardGame.Deck()
    main_deck.shuffle()
    for c in main_deck.card_list:
        print(c)
    player1 = CardGame.Player("Alice", 5)
    player2 = CardGame.Player("Bob", 5)
    for _ in range(5):
        player1.draw_card(main_deck)
        player2.draw_card(main_deck)
    print("{}'s hand:".format(player1.name))
    player1.show_hand()
    print("{}'s hand:".format(player2.name))
    player2.show_hand()


if __name__ == "__main__":
    main()
