# 2048-game

## Description of python files
The following python files contain the respective information.

1) GameManager.py. This is the driver program that loads the Computer AI and Player AI, and begins a game where they compete with each other. See below on how to execute this program.
2) Grid.py. This module defines the Grid object, along with some useful operations: move(), getAvailableCells(), insertTile(), and clone().
3) BaseAI.py. This is the base class for any AI component. All AIs inherit from this module, and implement the getMove() function, which takes a Grid object as parameter and returns a move (there are different "moves" for different AIs).
4) ComputerAI.py. This inherits from BaseAI. The getMove() function returns a computer action that is a tuple (x, y) indicating the place you want to place a tile.
5) PlayerAI.py. This should inherit from BaseAI. The getMove() function, which needs to implemented, returns a number that indicates the player’s action. In particular, 0 stands for "Up", 1 stands for "Down", 2 stands for "Left", and 3 stands for "Right". This file contains the heuristic for the game.
6) BaseDisplayer.py and Displayer.py. These print the grid.

To test the code, execute the game manager like so:
$ python GameManager.py
The progress of the game will be displayed on the terminal screen, with one snapshot printed after each move that the Computer AI or Player AI makes. The Player AI is allowed 0.2 seconds to come up with each move. The process continues until the game is over; that is, until no further legal moves can be made. At the end of the game, the maximum tile value on the board is printed.

## Screenshot of the algorithm in action
![Sample](https://user-images.githubusercontent.com/81757215/160060099-cac84703-1855-4eb8-b33b-0c772e3699b8.JPG)

## Screenshot of the final grid
![4096 screenshot](https://user-images.githubusercontent.com/81757215/160060080-fd80fdd4-63d4-4699-a309-c7463ba38225.JPG)
