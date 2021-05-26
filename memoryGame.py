# Peter Woon-Fat
# Memory Card Game
# Pairs of cards are randomly arranged across a grid. They are originally face up for player to see for a few seconds then turned face down
# and the player must find the matching pairs within the time limit - each matched pair gives 1 point.

# import modules used for memory game
import random
import tkinter as tk

# declare class containing gui component objects and functions to modify gui
# add changing between frames (intro w/ rules, game, scoreboard) in future
# can use Toplevel() to create new window displaying rules and high score respectively
class Window:
    def __init__(self):
        root = tk.Tk()
        root.title('MEMORY GAME')
        mainFrame = tk.Frame(root)
        mainFrame.pack(pady=10, padx=10)
        turnStr = tk.StringVar()
        turnLabel = tk.Label(mainFrame, textvariable=turnStr, underline=1).grid(row=0, column=0)
    def update_turnLabel(self, turn, points):
        self.turnStr.set(f'Turn {turn} - {points}pts')
    def set_card_grid(self, cards):
        pass

# declare class for card objects
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
        if self.is_matched():
            return 'x'
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
        playerGuess = 0
        while playerGuess < 1 or playerGuess > 16 or cards[playerGuess-1].is_matched():
            try:
                playerGuess = int(input('Enter the index of the first card you want to reveal: '))
                print('\n')
            except ValueError:
                continue
        return playerGuess - 1
    else:
        playerGuess = 0
        while playerGuess < 1 or playerGuess > 16 or cards[playerGuess-1].is_selected() or cards[playerGuess-1].is_matched():
            try:
                playerGuess = int(input('Enter the index of the second card you want to reveal: '))
                print('\n')
            except ValueError:
                continue
        return playerGuess - 1

# function prints a header introducing the game
def print_header():
    headerStr = '''
    ---Welcome to Peter's Memory Game!---
    ---There are 8 pairs of cards with matching letters---
    ---Finding the matching pairs to earn points!---
    ---Remember you can only turn over 2 cards at a time---
    --- > x = matched card---
    --- > - = face down card---
    '''
    print(headerStr.center(55))

# functions prints a grid with the 12 cards and their respective indexes
def print_cards(cards):
    indexCounter = 0
    for i in range(1, 5):
        cardRow = f'{cards[indexCounter].reveal()}\t{cards[indexCounter+1].reveal()}\t{cards[indexCounter+2].reveal()}\t{cards[indexCounter+3].reveal()}'
        indexRow = f'{indexCounter+1}\t{indexCounter+2}\t{indexCounter+3}\t{indexCounter+4}\n'
        print(cardRow.center(40))
        if i < 3:
            print(indexRow.center(40))
        else:
            print(indexRow.center(44))
        indexCounter = indexCounter + 4

# function sets all selected cards from previous turn to unselected to reset them for next turn
# takes list containing all cards as parameter
def unselect_all(cards):
    for c in cards:
        if c.is_selected():
            c.set_unselected()

# function loops through list containing all cards and checks if they are all matched
# takes list of cards as parameter
# returns True if all cards matched, otherwise returns False
def check_all_matched(cards, turn):
    for c in cards:
        if c.is_matched() == False:
            return False
    print(f'Congradulations you\'ve found all the matching cards in {turn} turns!')
    return True

# function prints the current turn and current number of points player has
def print_turn(turn, points):
    print('-' * 55)
    print(f'[Turn {turn}: {points}pts]')

# main code body, calls other functions to perform operations
if __name__ == '__main__':
    print_header()
    # declare variables used in game
    playerPoints = 0
    turnCounter = 1
    guess1, guess2 = 0, 0
    # initialize list containing cards with randomized positions
    cardsInPlay = initialize_cards()
    print_turn(turnCounter, playerPoints)
    # loop to ask player for guesses until all cards successfully matched
    while check_all_matched(cardsInPlay, turnCounter) == False:
        for i in range(1, 3):
            print_cards(cardsInPlay)
            if i == 1:
                guess1 = get_guess(cardsInPlay.copy(), i, 16)
                cardsInPlay[guess1].set_selected()
            if i == 2:
                guess2 = get_guess(cardsInPlay.copy(), i, 16)
                cardsInPlay[guess2].set_selected()
        print_cards(cardsInPlay)
        # check if cards player guessed are match and update points if so
        if cardsInPlay[guess1].letter == cardsInPlay[guess2].letter:
            cardsInPlay[guess1].set_matched()
            cardsInPlay[guess2].set_matched()
            playerPoints = playerPoints + 1
            print(f'+1 points - you found a matching pair!\n[You now have {playerPoints} points]')
        else:
            cardsInPlay[guess1].set_unselected()
            cardsInPlay[guess2].set_unselected()
        turnCounter = turnCounter + 1
        print_turn(turnCounter, playerPoints)