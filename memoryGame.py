# Peter Woon-Fat
# Memory Card Game
# Pairs of cards are randomly arranged across a grid. They are originally face up for player to see for a few seconds then turned face down
# and the player must find the matching pairs within the time limit - each matched pair gives 1 point.

# import modules used for memory game
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import DISABLED, FLAT, GROOVE, NORMAL, SUNKEN

# parent class for all GUI components of other 2 frames
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MEMORY GAME')
        self.resizable(False, False)

        self.gameFrame = Window(self)

    # function makes menu frame visible
    def show_menu(self):
        self.gameFrame.destroy()
        self.menuFrame = MainMenu(self, self.gameFrame.turn, self.gameFrame.points, self.gameFrame.submitBool)

# class initializes GUI and backend components for the memory game
# frame that player interacts with to play
class Window(tk.Frame):
    def __init__(self, container):
        self.container = container
        super().__init__(self.container)
        self.grid(row=0, column=1)
        ttk.Style().configure('Card.TButton', height=15, width=5, padding=2, relief=FLAT)

        self.turn, self.points = 1, 0
        self.submitBool = None
        self.cardsList = self.initialize_cards()
        self.selectedList = []
        self.set_initial_ui()
        self.container.after(4000, self.facedown_all)

    # function creates all initial GUI components for game window and initializes variables for calculating points
    def set_initial_ui(self):
        # initialize vars for calculating points
        self.earlyMatchBonus = True
        self.matchStreak = 0

        self.turnLabel = ttk.Label(self, text='Turn 1 - 0pts')
        self.turnLabel.grid(row=0, column=0, padx=10, pady=10) 
        self.statusLabel = ttk.Label(self, text='>>Choose a card<<')
        self.statusLabel.grid(row=0, column=2, columnspan=2, pady=10)

        # create buttons and labels used to represent cards and store in list, cards begin face up for first 4s
        self.cardBtn1 = ttk.Button(self, text=self.cardsList[0].letter, command=lambda:self.reveal(0), state=DISABLED, style='Card.TButton')
        self.cardBtn1.grid(row=1, column=1, ipady=30, padx=10)
        self.cardBtn2 = ttk.Button(self, text=self.cardsList[1].letter, command=lambda:self.reveal(1), state=DISABLED, style='Card.TButton')
        self.cardBtn2.grid(row=1, column=2, ipady=30, padx=10)
        self.cardBtn3 = ttk.Button(self, text=self.cardsList[2].letter, command=lambda:self.reveal(2), state=DISABLED, style='Card.TButton')
        self.cardBtn3.grid(row=1, column=3, ipady=30, padx=10)
        self.cardBtn4 = ttk.Button(self, text=self.cardsList[3].letter, command=lambda:self.reveal(3), state=DISABLED, style='Card.TButton')
        self.cardBtn4.grid(row=1, column=4, ipady=30, padx=10)
        self.cardBtn5 = ttk.Button(self, text=self.cardsList[4].letter, command=lambda:self.reveal(4), state=DISABLED, style='Card.TButton')
        self.cardBtn5.grid(row=3, column=1, ipady=30, padx=10)
        self.cardBtn6 = ttk.Button(self, text=self.cardsList[5].letter, command=lambda:self.reveal(5), state=DISABLED, style='Card.TButton')
        self.cardBtn6.grid(row=3, column=2, ipady=30, padx=10)
        self.cardBtn7 = ttk.Button(self, text=self.cardsList[6].letter, command=lambda:self.reveal(6), state=DISABLED, style='Card.TButton')
        self.cardBtn7.grid(row=3, column=3, ipady=30, padx=10)
        self.cardBtn8 = ttk.Button(self, text=self.cardsList[7].letter, command=lambda:self.reveal(7), state=DISABLED, style='Card.TButton')
        self.cardBtn8.grid(row=3, column=4, ipady=30, padx=10)
        self.cardBtn9 = ttk.Button(self, text=self.cardsList[8].letter, command=lambda:self.reveal(8), state=DISABLED, style='Card.TButton')
        self.cardBtn9.grid(row=5, column=1, ipady=30, padx=10)
        self.cardBtn10 = ttk.Button(self, text=self.cardsList[9].letter, command=lambda:self.reveal(9), state=DISABLED, style='Card.TButton')
        self.cardBtn10.grid(row=5, column=2, ipady=30, padx=10)
        self.cardBtn11 = ttk.Button(self, text=self.cardsList[10].letter, command=lambda:self.reveal(10), state=DISABLED, style='Card.TButton')
        self.cardBtn11.grid(row=5, column=3, ipady=30, padx=10)
        self.cardBtn12 = ttk.Button(self, text=self.cardsList[11].letter, command=lambda:self.reveal(11), state=DISABLED, style='Card.TButton')
        self.cardBtn12.grid(row=5, column=4, ipady=30, padx=10)
        self.cardBtn13 = ttk.Button(self, text=self.cardsList[12].letter, command=lambda:self.reveal(12), state=DISABLED, style='Card.TButton')
        self.cardBtn13.grid(row=7, column=1, ipady=30, padx=10)
        self.cardBtn14 = ttk.Button(self, text=self.cardsList[13].letter, command=lambda:self.reveal(13), state=DISABLED, style='Card.TButton')
        self.cardBtn14.grid(row=7, column=2, ipady=30, padx=10)
        self.cardBtn15 = ttk.Button(self, text=self.cardsList[14].letter, command=lambda:self.reveal(14), state=DISABLED, style='Card.TButton')
        self.cardBtn15.grid(row=7, column=3, ipady=30, padx=10)
        self.cardBtn16 = ttk.Button(self, text=self.cardsList[15].letter, command=lambda:self.reveal(15), state=DISABLED, style='Card.TButton')
        self.cardBtn16.grid(row=7, column=4, ipady=30, padx=10)
        
        self.cardLbl1 = ttk.Label(self, text='Card 1')
        self.cardLbl1.grid(row=2, column=1, pady=5)
        self.cardLbl2 = ttk.Label(self, text='Card 2')
        self.cardLbl2.grid(row=2, column=2, pady=5)
        self.cardLbl3 = ttk.Label(self, text='Card 3')
        self.cardLbl3.grid(row=2, column=3, pady=5)
        self.cardLbl4 = ttk.Label(self, text='Card 4')
        self.cardLbl4.grid(row=2, column=4, pady=5)
        self.cardLbl5 = ttk.Label(self, text='Card 5')
        self.cardLbl5.grid(row=4, column=1, pady=5)
        self.cardLbl6 = ttk.Label(self, text='Card 6')
        self.cardLbl6.grid(row=4, column=2, pady=5)
        self.cardLbl7 = ttk.Label(self, text='Card 7')
        self.cardLbl7.grid(row=4, column=3, pady=5)
        self.cardLbl8 = ttk.Label(self, text='Card 8')
        self.cardLbl8.grid(row=4, column=4, pady=5)
        self.cardLbl9 = ttk.Label(self, text='Card 9')
        self.cardLbl9.grid(row=6, column=1, pady=5)
        self.cardLbl10 = ttk.Label(self, text='Card 10')
        self.cardLbl10.grid(row=6, column=2, pady=5)
        self.cardLbl11 = ttk.Label(self, text='Card 11')
        self.cardLbl11.grid(row=6, column=3, pady=5)
        self.cardLbl12 = ttk.Label(self, text='Card 12')
        self.cardLbl12.grid(row=6, column=4, pady=5)
        self.cardLbl13 = ttk.Label(self, text='Card 13')
        self.cardLbl13.grid(row=8, column=1, pady=5)
        self.cardLbl14 = ttk.Label(self, text='Card 14')
        self.cardLbl14.grid(row=8, column=2, pady=5)
        self.cardLbl15 = ttk.Label(self, text='Card 15')
        self.cardLbl15.grid(row=8, column=3, pady=5)
        self.cardLbl16 = ttk.Label(self, text='Card 16')
        self.cardLbl16.grid(row=8, column=4, pady=5)
        self.cardBtnList = [self.cardBtn1, self.cardBtn2, self.cardBtn3, self.cardBtn4, self.cardBtn5, self.cardBtn6, self.cardBtn7, self.cardBtn8, self.cardBtn9, self.cardBtn10, self.cardBtn11, self.cardBtn12, self.cardBtn13, self.cardBtn14, self.cardBtn15, self.cardBtn16]
        self.CardLblList = [self.cardLbl1, self.cardLbl2, self.cardLbl3, self.cardLbl4, self.cardLbl5, self.cardLbl7, self.cardLbl8, self.cardLbl9, self.cardLbl10, self.cardLbl11, self.cardLbl12, self.cardLbl13, self.cardLbl14, self.cardLbl15, self.cardLbl16]
    
    # function updates the text of the turn and points label
    def update_turnLabel(self):
        self.turnLabel.configure(text=f'Turn {self.turn} - {self.points}pts')

    def update_statusLabel(self, status):
        self.statusLabel.configure(text=status)
    
    # after a set time, function is called to set all cards face down to begin game
    def facedown_all(self):
        for b in self.cardBtnList:
            b.configure(text='?', state=NORMAL)
    
    # when a card is selected (button pressed), show its letter and set state to disabled
    def reveal(self, index):
        self.cardBtnList[index].configure(text=self.cardsList[index].letter, state=DISABLED)
        self.cardsList[index].set_selected()
        self.selectedList.append(index)

        if len(self.selectedList) == 1:
            self.update_statusLabel('>>Choose a second card<<')
        if len(self.selectedList) == 2:
            self.check_pair_match()
        if len(self.selectedList) > 2:
            self.reset_selected()

    # function sets cards back facedown after unsuccessful match
    def unreveal(self):
        self.cardBtnList[self.selectedList[0]].configure(text='?', state=NORMAL)
        self.cardBtnList[self.selectedList[1]].configure(text='?', state=NORMAL)
        self.cardsList[self.selectedList[0]].set_unselected()
        self.cardsList[self.selectedList[1]].set_unselected()
        self.selectedList.clear()

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

    # function returns true if the 2 selected cards have matching letters, otherwise returns false
    def check_pair_match(self):
        # selected cards match, update GUI and points
        if self.cardsList[self.selectedList[0]].letter == self.cardsList[self.selectedList[1]].letter:
            self.update_statusLabel('>>You found a match! Choose another card<<')
            self.cardsList[self.selectedList[0]].set_unselected()
            self.cardsList[self.selectedList[1]].set_unselected()
            self.cardsList[self.selectedList[0]].set_matched()
            self.cardsList[self.selectedList[1]].set_matched()
            self.cardBtnList[self.selectedList[0]].configure(text=f'{self.cardsList[self.selectedList[0]].letter.center(10)}')
            self.cardBtnList[self.selectedList[1]].configure(text=f'{self.cardsList[self.selectedList[1]].letter.center(10)}')
            self.points += self.add_points()
            self.matchStreak += 1
            self.selectedList.clear()
        # selected cards do not match, reset matchStreak
        else:
            self.earlyMatchBonus = False
            self.matchStreak = 0
            self.container.after(500, self.unreveal)
            self.update_statusLabel('>>Choose a card<<')
        
        # check if all cards have been matched (game over)
        if self.check_all_matched():
            self.statusLabel.configure(text='Congradulations you found all the matching cards!')
            self.submitBool = messagebox.askyesno('Submit Score', 'Do you want to submit your score to be placed on the high scores ranking?')
            # show menu frame with replay and quit buttons and high scores
            self.container.show_menu()
        else:
            self.turn += 1
            self.update_turnLabel()

    # function returns true if all cards have been matched, otherwise returns false
    def check_all_matched(self):
        for c in self.cardsList:
            if c.is_matched() == False:
                return False
        return True

    # function checks if player has selected more than 2 cards at once and sets extras back to normal
    def reset_selected(self):
        for i in self.selectedList[2:]:
            self.cardsList[i].set_unselected()
            self.cardBtnList[i].configure(text='?', state=NORMAL)

    # function calculates the amount of points the player should be given based on set of rules
    def add_points(self):
        pointsCalculated = 1 + self.matchStreak
        if self.earlyMatchBonus:
            pointsCalculated += 3
        return pointsCalculated

# class initializes components for the high scores labelframe
# occupies left side of app window once player completes game
class MainMenu(tk.Frame):
    def __init__(self, container, turn, points, submitBool):
        self.container = container
        super().__init__(self.container)
        self.grid(row=0, column=0)

        self.set_menu_buttons()
        if submitBool:
            self.turn = turn
            self.points = points
            self.set_menu_entry()
        
        self.display_scores()
    
    # function creates play again and reset buttons
    def set_menu_buttons(self):
        self.playAgainBtn = ttk.Button(self, text='Play Again')
        self.playAgainBtn.grid(row=0, padx=10, pady=10)
        self.quitBtn = ttk.Button(self, text='Quit', command=quit)
        self.quitBtn.grid(row=1, padx=10, pady=10)

    # function creates entry widget and submit button for player to enter their username and submit it with their score
    def set_menu_entry(self):
        self.nameEntry = ttk.Entry(self)
        self.nameEntry.insert(0, 'Username')
        self.nameEntry.grid(row=2, rowspan=2, sticky='s')
        self.nameEntry.focus()
        self.submitBtn = ttk.Button(self, text='Submit', command=lambda: self.submit_score(self.nameEntry.get(), self.turn, self.points))
        self.submitBtn.grid(row=4)

    # function creates another labelframe for high scores, contained inside main menu labelframe
    def display_scores(self):
        ttk.Style().configure('HSTable.TLabelframe', relief=SUNKEN, bd=4)
        hsLabelFrame = ttk.LabelFrame(self, text='Top Scores', style='HSTable.TLabelframe')
        hsLabelFrame.grid(row=5)
        self.get_scores()

        self.scoreLbl1 = ttk.Label(hsLabelFrame, text=f'1. {self.usernameList[self.topScoresList[0]]} - {self.pointsList[self.topScoresList[0]]}pts [turn {self.turnList[self.topScoresList[0]]}]')
        self.scoreLbl1.grid(row=0)
        self.scoreLbl1 = ttk.Label(hsLabelFrame, text=f'2. {self.usernameList[self.topScoresList[1]]} - {self.pointsList[self.topScoresList[1]]}pts [turn {self.turnList[self.topScoresList[1]]}]')
        self.scoreLbl1.grid(row=1)
        self.scoreLbl1 = ttk.Label(hsLabelFrame, text=f'3. {self.usernameList[self.topScoresList[2]]} - {self.pointsList[self.topScoresList[2]]}pts [turn {self.turnList[self.topScoresList[2]]}]')
        self.scoreLbl1.grid(row=2)
        self.scoreLbl1 = ttk.Label(hsLabelFrame, text=f'4. {self.usernameList[self.topScoresList[3]]} - {self.pointsList[self.topScoresList[3]]}pts [turn {self.turnList[self.topScoresList[3]]}]')
        self.scoreLbl1.grid(row=3)
        self.scoreLbl1 = ttk.Label(hsLabelFrame, text=f'5. {self.usernameList[self.topScoresList[4]]} - {self.pointsList[self.topScoresList[4]]}pts [turn {self.turnList[self.topScoresList[4]]}]')
        self.scoreLbl1.grid(row=4)

    # function reads through highscores.txt line by line and stores top 5 scores in a list of tuples to display
    def get_scores(self):
        self.usernameList = []
        self.pointsList = []
        self.turnList = []
        self.topScoresList = []

        with open('highscores.txt') as fp:
            dataLine = fp.readline()
            dataLine.replace('\n', '')
            dataList = []
            while dataLine != '':
                dataList = dataLine.split()
                self.usernameList.append(dataList[0])
                self.pointsList.append(int(dataList[1]))
                self.turnList.append(dataList[2])
                dataList.clear()
                dataLine = fp.readline()

        for i in range(5):
            topScore = 0
            topScoreIndex = 0
            for j in range(len(self.pointsList)):
                if self.pointsList[j] > topScore:
                    topScore = self.pointsList[j]
                    topScoreIndex = j
                    self.usernameList.pop(j)
                    self.pointsList.pop(j)
                    self.turnList.pop(j)
            self.topScoresList.insert(i, topScoreIndex)

    # function writes current player username, points, and turn to highscores.txt
    def submit_score(self, username, turn, points):
        with open('highscores.txt', 'a') as fp:
            fp.write(f'{username} {points} {turn}\n')

    def reset_game(self):
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

# function creates a message box telling the player the rules before game begins
def show_rules():
    messagebox.showinfo('RULES', '''
    Welcome to Peter's Memory Game!
    There are 8 pairs of cards with matching letters
    Find the matching pairs to earn points within the least amount of turns!
    Remember you can only turn over 2 cards at a time

    >>When you press okay you will have 5 seconds to memorize the cards' positions<<
    ''')

if __name__ == '__main__':
    show_rules()
    app = App()
    app.mainloop()