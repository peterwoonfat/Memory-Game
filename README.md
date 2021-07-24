<pre>
Author: Peter Woon-Fat
File Name: memoryGame.py
Run with: python memoryGame.py

Game Description:
  When the program starts, a precursory tkinter window listing the rules and describing the game will pop up. Once the player pressed the "OK" button, the window will
  disappear and another window titled "MEMORY GAME" (the main user interface for the game) will appear and the player can begin their game.
  The userface contains an array of buttons, each representing a card, for the player to click on and reveal the letter underneath. The player selected two cards at once,
  meaning only two letters will be visible to the player at once. There are 8 pairs of letters randomly scrambled which the player will have to reveal. When the player finds
  a match, points will be given (the amount of points given varies depending on the conditions mentioned in the game's "RULES" window.
  The player can view the current turn and point counts in the top left of the "MEMORY GAME" window. In the top center of the "MEMORY GAME" window there is a label with text
  guiding the player on what they should be doing as well as alerting the player when a match is found.
  Once all the cards have been matched, the "MEMORY GAME" window expands, adding a new menu on the left side of the window. There is a "Play Again" button to restart the game,
  as well as a "Quit" button to close the window. The player also has the option to enter a username in the input box and upon pressing the "Submit" button directly underneath,
  the player's username, along with their turn and point counts will be saved in "highscores.txt". The top five saved high scores will be dispayed in the "Top Scores" 
  table directly underneath the submit button.
  
Notes:
  This project was made to gain some practical experience with Python as I was learning the language for the first time. I was able to apply my understanding of object oriented
  programming concepts such as inheritence, as well as gain experience with Python's data structures.
  After completing the program with console playability, I wanted the learn about some GUI tools and decided to use Python's tkinter(due to its easy accesibilty) to give my
  program a GUI.
  Overall I am proud of how my program turned out and I found this to be a very valuable learning experience, especially tkinter helping me to understand and apply 
  object oriented concepts.
  </pre>
