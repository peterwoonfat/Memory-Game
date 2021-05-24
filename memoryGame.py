# Peter Woon-Fat
# Memory Card Game
# Pairs of cards are randomly arranged across a grid. They are originally face up for player to see for a few seconds then turned face down
# and the player must find the matching pairs within the time limit - each matched pair gives 1 point.

# import modules used for memory game
import random

# declare initialize class for card objects
# player can select up to 2 cards at once, stored in a list
# when card is selected it is turned face up until either matching pair found then it dissappears or unsuccessful match and both cards unselected
class Card:
    def __init__(self, letter):
        self.letter = letter
        self.selected = False
        self.matched = False
    def set_selected(self):
        self.selected = True
    def set_unselected(self):
        self.selected = False
    def is_selected(self):
        if self.selected == True:
            return True
        return False
    def set_matched(self):
        self.matched = True
    def is_matched(self):
        if self.matched == True:
            return True
        return False
    def reveal(self):
        if self.selected == True:
            return self.letter
        return '-'


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
    return set_positions(cardList, 16)

# function takes list of card objects and randomizes positions in list
def set_positions(cards, numCards):
    return list(random.sample(cards, numCards))

# make function to take player guess
def get_guess(cards, num, limit):
    if num == 1:
        playerGuess = int(input('Enter the index of the first card you want to reveal: '))
        while playerGuess < 1 or playerGuess > 16 or cards[playerGuess].is_matched():
            playerGuess = int(input('Enter the index of the first card you want to reveal: '))
        return playerGuess
    else:
        playerGuess = int(input('Enter the index of the second card you want to reveal: '))
        while playerGuess < 1 or playerGuess > 16 or cards[playerGuess].is_selected() or cards[playerGuess].is_matched():
            playerGuess = int(input('Enter the index of the second card you want to reveal: '))
        return playerGuess

def print_header():
    headerStr = '''
    ---Welcome to Peter's Memory Game!---
    ---There are 8 pairs of cards with matching letters---
    ---Finding the matching pairs to earn points!---
    ---Remember you can only turn over 2 cards at a time---
    '''
    print(headerStr.center(55))

def print_cards():
    pass

# main code body, calls other functions to perform operations
if __name__ == '__main__':
    print_header()
    playerPoints = 0
    cardsInPlay = initialize_cards()
    while len(cardsInPlay) != 0:
        guess1 = get_guess(cardsInPlay.copy(), 1, 16)
        cardsInPlay[guess1].set_selected()
        guess2 = get_guess(cardsInPlay.copy(), 2, 16)
        cardsInPlay[guess2].set_selected()
        if cardsInPlay[guess1].letter == cardsInPlay[guess2].letter:
            cardsInPlay[guess1].set_matched()
            cardsInPlay[guess2].set_matched()
            playerPoints = playerPoints + 1