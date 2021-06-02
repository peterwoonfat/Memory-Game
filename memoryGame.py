# Peter Woon-Fat
# Memory Card Game
# Pairs of cards are randomly arranged across a grid. They are originally face up for player to see for a few seconds then turned face down
# and the player must find the matching pairs within the time limit - each matched pair gives 1 point.

# import modules used for memory game
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import DISABLED, NORMAL

# declare class containing gui component objects and functions to modify gui
# add changing between frames (intro w/ rules, game, scoreboard) in future
# can use Toplevel() to create new window displaying rules and high score respectively
# grid: row 0 - 5, col 0 - 4
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MEMORY GAME')
        self.style = ttk.Style(self)
        self.style.configure('TButton', )

class Window(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.turn, self.points = 1, 0
        self.cardsList = self.initialize_cards()
        self.selectedList = []
        self.set_initial_ui(container)
        container.after(4000, self.facedown_all)

    def set_initial_ui(self, container):
        self.turnLabel = ttk.Label(container, text='Turn 1 - 0pts')
        self.turnLabel.grid(row=0, column=0, padx=10, pady=10)
        # declare buttons and labels used to represent cards and store in list, cards begin face up for first 5s
        self.cardBtn1 = ttk.Button(container, text=self.cardsList[0].letter, command=lambda:self.reveal(0, container), state=DISABLED)
        self.cardBtn1.grid(row=1, column=1, ipady=30, padx=10)
        self.cardBtn2 = ttk.Button(container, text=self.cardsList[1].letter, command=lambda:self.reveal(1, container), state=DISABLED)
        self.cardBtn2.grid(row=1, column=2, ipady=30, padx=10)
        self.cardBtn3 = ttk.Button(container, text=self.cardsList[2].letter, command=lambda:self.reveal(2, container), state=DISABLED)
        self.cardBtn3.grid(row=1, column=3, ipady=30, padx=10)
        self.cardBtn4 = ttk.Button(container, text=self.cardsList[3].letter, command=lambda:self.reveal(3, container), state=DISABLED)
        self.cardBtn4.grid(row=1, column=4, ipady=30, padx=10)
        self.cardBtn5 = ttk.Button(container, text=self.cardsList[4].letter, command=lambda:self.reveal(4, container), state=DISABLED)
        self.cardBtn5.grid(row=3, column=1, ipady=30, padx=10)
        self.cardBtn6 = ttk.Button(container, text=self.cardsList[5].letter, command=lambda:self.reveal(5, container), state=DISABLED)
        self.cardBtn6.grid(row=3, column=2, ipady=30, padx=10)
        self.cardBtn7 = ttk.Button(container, text=self.cardsList[6].letter, command=lambda:self.reveal(6, container), state=DISABLED)
        self.cardBtn7.grid(row=3, column=3, ipady=30, padx=10)
        self.cardBtn8 = ttk.Button(container, text=self.cardsList[7].letter, command=lambda:self.reveal(7, container), state=DISABLED)
        self.cardBtn8.grid(row=3, column=4, ipady=30, padx=10)
        self.cardBtn9 = ttk.Button(container, text=self.cardsList[8].letter, command=lambda:self.reveal(8, container), state=DISABLED)
        self.cardBtn9.grid(row=5, column=1, ipady=30, padx=10)
        self.cardBtn10 = ttk.Button(container, text=self.cardsList[9].letter, command=lambda:self.reveal(9, container), state=DISABLED)
        self.cardBtn10.grid(row=5, column=2, ipady=30, padx=10)
        self.cardBtn11 = ttk.Button(container, text=self.cardsList[10].letter, command=lambda:self.reveal(10, container), state=DISABLED)
        self.cardBtn11.grid(row=5, column=3, ipady=30, padx=10)
        self.cardBtn12 = ttk.Button(container, text=self.cardsList[11].letter, command=lambda:self.reveal(11, container), state=DISABLED)
        self.cardBtn12.grid(row=5, column=4, ipady=30, padx=10)
        self.cardBtn13 = ttk.Button(container, text=self.cardsList[12].letter, command=lambda:self.reveal(12, container), state=DISABLED)
        self.cardBtn13.grid(row=7, column=1, ipady=30, padx=10)
        self.cardBtn14 = ttk.Button(container, text=self.cardsList[13].letter, command=lambda:self.reveal(13, container), state=DISABLED)
        self.cardBtn14.grid(row=7, column=2, ipady=30, padx=10)
        self.cardBtn15 = ttk.Button(container, text=self.cardsList[14].letter, command=lambda:self.reveal(14, container), state=DISABLED)
        self.cardBtn15.grid(row=7, column=3, ipady=30, padx=10)
        self.cardBtn16 = ttk.Button(container, text=self.cardsList[15].letter, command=lambda:self.reveal(15, container), state=DISABLED)
        self.cardBtn16.grid(row=7, column=4, ipady=30, padx=10)
        self.cardLbl1 = ttk.Label(container, text='Card 1')
        self.cardLbl1.grid(row=2, column=1, pady=5)
        self.cardLbl2 = ttk.Label(container, text='Card 2')
        self.cardLbl2.grid(row=2, column=2, pady=5)
        self.cardLbl3 = ttk.Label(container, text='Card 3')
        self.cardLbl3.grid(row=2, column=3, pady=5)
        self.cardLbl4 = ttk.Label(container, text='Card 4')
        self.cardLbl4.grid(row=2, column=4, pady=5)
        self.cardLbl5 = ttk.Label(container, text='Card 5')
        self.cardLbl5.grid(row=4, column=1, pady=5)
        self.cardLbl6 = ttk.Label(container, text='Card 6')
        self.cardLbl6.grid(row=4, column=2, pady=5)
        self.cardLbl7 = ttk.Label(container, text='Card 7')
        self.cardLbl7.grid(row=4, column=3, pady=5)
        self.cardLbl8 = ttk.Label(container, text='Card 8')
        self.cardLbl8.grid(row=4, column=4, pady=5)
        self.cardLbl9 = ttk.Label(container, text='Card 9')
        self.cardLbl9.grid(row=6, column=1, pady=5)
        self.cardLbl10 = ttk.Label(container, text='Card 10')
        self.cardLbl10.grid(row=6, column=2, pady=5)
        self.cardLbl11 = ttk.Label(container, text='Card 11')
        self.cardLbl11.grid(row=6, column=3, pady=5)
        self.cardLbl12 = ttk.Label(container, text='Card 12')
        self.cardLbl12.grid(row=6, column=4, pady=5)
        self.cardLbl13 = ttk.Label(container, text='Card 13')
        self.cardLbl13.grid(row=8, column=1, pady=5)
        self.cardLbl14 = ttk.Label(container, text='Card 14')
        self.cardLbl14.grid(row=8, column=2, pady=5)
        self.cardLbl15 = ttk.Label(container, text='Card 15')
        self.cardLbl15.grid(row=8, column=3, pady=5)
        self.cardLbl16 = ttk.Label(container, text='Card 16')
        self.cardLbl16.grid(row=8, column=4, pady=5)
        self.cardBtnList = [self.cardBtn1, self.cardBtn2, self.cardBtn3, self.cardBtn4, self.cardBtn5, self.cardBtn6, self.cardBtn7, self.cardBtn8, self.cardBtn9, self.cardBtn10, self.cardBtn11, self.cardBtn12, self.cardBtn13, self.cardBtn14, self.cardBtn15, self.cardBtn16]
        self.CardLblList = [self.cardLbl1, self.cardLbl2, self.cardLbl3, self.cardLbl4, self.cardLbl5, self.cardLbl7, self.cardLbl8, self.cardLbl9, self.cardLbl10, self.cardLbl11, self.cardLbl12, self.cardLbl13, self.cardLbl14, self.cardLbl15, self.cardLbl16]
    
    def update_turnLabel(self):
        self.turnLabel.configure(text=f'Turn {self.turn} - {self.points}pts')
    
    # after a set time, function is called to set all cards face down to begin game
    def facedown_all(self):
        self.cardBtn1.configure(text='?', state=NORMAL)
        self.cardBtn2.configure(text='?', state=NORMAL)
        self.cardBtn3.configure(text='?', state=NORMAL)
        self.cardBtn4.configure(text='?', state=NORMAL)
        self.cardBtn5.configure(text='?', state=NORMAL)
        self.cardBtn6.configure(text='?', state=NORMAL)
        self.cardBtn7.configure(text='?', state=NORMAL)
        self.cardBtn8.configure(text='?', state=NORMAL)
        self.cardBtn9.configure(text='?', state=NORMAL)
        self.cardBtn10.configure(text='?', state=NORMAL)
        self.cardBtn11.configure(text='?', state=NORMAL)
        self.cardBtn12.configure(text='?', state=NORMAL)
        self.cardBtn13.configure(text='?', state=NORMAL)
        self.cardBtn14.configure(text='?', state=NORMAL)
        self.cardBtn15.configure(text='?', state=NORMAL)
        self.cardBtn16.configure(text='?', state=NORMAL)
    
    # when a card is selected (button pressed), show its letter and set state to disabled
    def reveal(self, index, container):
        self.cardBtnList[index].configure(text=self.cardsList[index].letter, state=DISABLED)
        self.cardsList[index].set_selected()
        self.selectedList.append(index)
        print(f'CARD ADDED - LEN {len(self.selectedList)}')
        if len(self.selectedList) == 2:
            self.check_pair_match(container)
            #self.check_two_selected()

    def unreveal(self):
        print(f'FINAL LEN {len(self.selectedList)}')
        self.cardBtnList[self.selectedList[0]].configure(text='?', state=NORMAL)
        self.cardBtnList[self.selectedList[1]].configure(text='?', state=NORMAL)
        self.cardsList[self.selectedList[0]].set_unselected()
        self.cardsList[self.selectedList[1]].set_unselected()

    # function creatles list of 16 cards (8 pairs) with a letter and their position in the grid
    def initialize_cards(self):
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
        return self.set_positions(cardList, 16)
    
    # function takes list of card objects and randomizes positions in list
    def set_positions(self, cards, numCards):
        return list(random.sample(cards, numCards))
    
    # function checks if user has selected 2 cards, if true then checks if match (if match then checks if all cards matched) and increments turn counter
    # def check_two_selected(self):
    #     selectedCount = 0
    #     for c in self.cardsList:
    #         if c.is_selected():
    #             selectedCount += 1
    #         if selectedCount == 2:
    #             if self.check_pair_match():
    #                 self.points += 1
    #                 if self.check_all_matched():
    #                     pass
    #             self.turn += 1
    #             self.update_turnLabel(self.turn, self.points)
    #             break

    # function returns true if the 2 selected cards have matching letters, otherwise returns false
    def check_pair_match(self, container):
        if self.cardsList[self.selectedList[0]].letter == self.cardsList[self.selectedList[1]].letter:
            self.cardsList[self.selectedList[0]].set_unselected()
            self.cardsList[self.selectedList[1]].set_unselected()
            self.cardsList[self.selectedList[0]].set_matched()
            self.cardsList[self.selectedList[1]].set_matched()
            self.cardBtnList[self.selectedList[0]].configure(text=f'{self.cardsList[self.selectedList[0]].letter}\n[matched]')
            self.cardBtnList[self.selectedList[1]].configure(text=f'{self.cardsList[self.selectedList[1]].letter}\n[matched]')
            self.points += 1
            self.selectedList.clear()
            # if self.check_all_matched():
            #     pass
        else:
            print(f'CHECK PRE LEN {len(self.selectedList)}')
            container.after(1000, self.unreveal)
        self.turn += 1
        self.update_turnLabel()

    # function returns true if all cards have been matched, otherwise returns false
    def check_all_matched(self):
        for c in self.cardsList:
            if c.is_matched() == False:
                return False
        return True

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

# function creates a message box telling the player the rules before game begins
def show_rules():
    messagebox.showinfo('RULES', '''
    Welcome to Peter's Memory Game!
    There are 8 pairs of cards with matching letters
    Find the matching pairs to earn points within the least amount of turns!
    Remember you can only turn over 2 cards at a time

    >>When you press okay you will have 5 seconds to memorize the cards' positions<<
    ''')

# # main code body, calls other functions to perform operations
# if __name__ == '__main__':
#     print_header()
#     # declare variables used in game
#     playerPoints = 0
#     turnCounter = 1
#     guess1, guess2 = 0, 0
#     # initialize list containing cards with randomized positions
#     cardsInPlay = initialize_cards()
#     print_turn(turnCounter, playerPoints)
#     # loop to ask player for guesses until all cards successfully matched
#     while check_all_matched(cardsInPlay, turnCounter) == False:
#         for i in range(1, 3):
#             print_cards(cardsInPlay)
#             if i == 1:
#                 guess1 = get_guess(cardsInPlay.copy(), i, 16)
#                 cardsInPlay[guess1].set_selected()
#             if i == 2:
#                 guess2 = get_guess(cardsInPlay.copy(), i, 16)
#                 cardsInPlay[guess2].set_selected()
#         print_cards(cardsInPlay)
#         # check if cards player guessed are match and update points if so
#         if cardsInPlay[guess1].letter == cardsInPlay[guess2].letter:
#             cardsInPlay[guess1].set_matched()
#             cardsInPlay[guess2].set_matched()
#             playerPoints = playerPoints + 1
#             print(f'+1 points - you found a matching pair!\n[You now have {playerPoints} points]')
#         else:
#             cardsInPlay[guess1].set_unselected()
#             cardsInPlay[guess2].set_unselected()
#         turnCounter = turnCounter + 1
#         print_turn(turnCounter, playerPoints)

if __name__ == '__main__':
    show_rules()
    app = App()
    gameFrame = Window(app)
    app.mainloop()