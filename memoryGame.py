# Peter Woon-Fat
# Memory Card Game
# Pairs of cards are randomly arranged across a grid. They are originally face up for player to see for a few seconds then turned face down
# and the player must find the matching pairs within the time limit - each matched pair gives 1 point.

# import modules
import random

# declare initialize class for card objects
# player can select up to 2 cards at once, stored in a list
# when card is selected it is turned face up until either matching pair found then it dissappears or unsuccessful match and both cards unselected
class Card:
    def __init__(self, letter):
        self.letter = letter
        self.selected = False
    def set_selected(self):
        self.selected = True
    def set_unselected(self):
        self.selected = False

# function initializes 16 cards (8 pairs) with a letter and their position in the grid
# returns list of cards
def initialize_cards():
    cardA1 = Card('A')
    cardA2 = Card('A')
    cardB1 = Card('B')
    cardB2 = Card('B')
    cardC1 = Card('C')
    cardC2 = Card('C')
    cardD1 = Card('D')
    cardD2 = Card('D')
    cardE1 = Card('E')
    cardE2 = Card('E')
    cardF1 = Card('F')
    cardF2 = Card('F')
    cardG1 = Card('G')
    cardG2 = Card('G')
    cardH1 = Card('H')
    cardH2 = Card('H')
    cardList = [cardA1, cardA2, cardB1, cardB2, cardC1, cardC2, cardD1, cardD2, cardE1, cardE2, cardF1, cardF2, cardG1, cardG2, cardH1, cardH2]
    return set_positions(cardList)

# function takes list of card objects and randomizes positions in list
def set_positions(cards):
    return list(random.sample(cards, 16))

# make function to take player guess
def get_guess(num):
    if num == 1:
        return input('Enter the index of the first card you want to reveal: ')
    else:
        return input('Enter the index of the second card you want to reveal: ')

# function sets specified card to selected
# takes the list of cards in play and the index of the player chosen card as parameters
def reveal_card(cards, index):
    cards[index].setSelected()

if __name__ == '__main__':
    cardsInPlay = initialize_cards()
    while len(cardGrid) != 0:
        guess1 = get_guess(1)
        reveal_card(guess1)
        guess2 = get_guess(2)
        reveal_card(guess2)