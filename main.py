# Game of Life  
# Author : Loïc Pottier
# Creation date : 12/01/2022

# IMPORTS
import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# CONSTANTS
SIZE=50
DELAY=1

DEAD=1
ALIVE=16
VALUES=[DEAD, ALIVE]


class Life:
    # main constructor
    # create a board filled with dead or alive values
    # chances are : 20% for alive and 80% for dead
    def __init__(self) -> None:
        self.finished = False
        self.board=np.random.choice(VALUES, SIZE*SIZE, p=[0.8, 0.2]).reshape(SIZE, SIZE)

    # return the amount of neighbours of a tile in (x, y)
    def getAlive(self, x, y) -> int:
        live=0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx==0 and dy==0:
                    pass
                else:
                    if self.board[(y+dy)%SIZE][(x+dx)%SIZE]==ALIVE:
                        live+=1
        return live

    # return the next state of the tile in (x, y)
    def getNextState(self, x, y) -> int:
        val=DEAD
        live=self.getAlive(x, y)
        if self.board[y][x]==DEAD:
            if live==3:
                val=ALIVE
        if self.board[y][x]==ALIVE:
            if live in (2, 3):
                val=ALIVE
        return val

    # update the board with the next state of each tile
    # and set the new data to the matplotlab img
    def nextTurn(self, frameNum, img):
        newBoard=[]
        # self.increaseSize()
        for y in range(len(self.board)):
            newBoard.append([])
            for x in range(len(self.board[y])):
                newBoard[y].append(self.getNextState(x, y))
                
        self.board=newBoard
        img.set_data(newBoard)
        return img
    
    # increase the size of the board, i don't use it
    # use it if you want don't want the board to be toroid 

    # need fix to work, 
    def increaseSize(self):
        if ALIVE in self.board[0]:
            np.insert(self.board, 0, [])
            for x in range(len(self.board[1])):
                np.insert(self.board, 0, DEAD)

        if ALIVE in self.board[-1]:
            np.append(self.board, [])
            for x in range(len(self.board[0])):
                np.append(self.board[-1], DEAD)

        for row in self.board:
            if row[0]==1:
                for dRow in range(len(self.board)):
                    np.insert(self.board[dRow], 0, DEAD)
                break     

        for row in self.board:
            if row[-1]==1:
                for dRow in range(len(self.board)):
                    np.append(self.board[dRow], len(self.board), DEAD)
                break               

    # add a glider on x, y position
    # glider is a special disposition in game of life that move in diagonal (direction depends on his orientation)
    def addGlider(self, x, y):
        glider = np.array([[0, 0, 1], 
                           [1, 0, 1], 
                           [0, 1, 1]])
        self.board[y:y+3, x:x+3] = glider

    # Return a printable form of the board attribute
    def __str__(self) -> str:
        os.system('cls')
        returnStr=""
        for y in self.board:
            for x in y:
                if x==0:
                    returnStr+="□"
                else:
                    returnStr+="■"
                returnStr+=" "
            returnStr+="\n"
        return returnStr

if __name__=="__main__":
    game=Life()

    fig, ax = plt.subplots()
    img = ax.imshow(game.board, cmap=mpl.colormaps['inferno'])
    ani = animation.FuncAnimation(fig, game.nextTurn, fargs=(img, ), frames=10, interval=DELAY)

    plt.show()