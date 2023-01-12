# Game of Life  
# Author : Loïc Pottier
# Creation date : 12/01/2022

# IMPORTS

import os
import time
import random

# CONSTANTS
BASE_HEIGHT=20
BASE_WIDTH=20

DELAY=0.25


class Life:


    # main constructor
    def __init__(self, board=None) -> None:
        self.board=[]
        self.finished = False

        if board==None:
            for y in range(BASE_HEIGHT):
                self.board.append([])
                for x in range(BASE_WIDTH):
                    self.board[y].append(0)
        else:
            self.board=board


    # return the amount of neighbors of a tile in (x, y)
    def getLiveNeighboursAmount(self, x, y) -> int:
        live=0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx==0 and dy==0:
                    pass
                else:
                    if 0<=x+dx<len(self.board[0]) and 0<=y+dy<len(self.board):
                        if self.board[y+dy][x+dx]==1:
                            live+=1
        return live


    # return the next state of the tile in (x, y)
    def getNextState(self, x, y) -> int:
        val=0
        live=self.getLiveNeighboursAmount(x, y)
        if self.board[y][x]==0:
            if live==3:
                val=1
        if self.board[y][x]==1:
            if live in (2, 3):
                val=1
        return val


    # update the board with the next state of each tile
    def nextTurn(self):
        newBoard=[]
        for y in range(len(self.board)):
            newBoard.append([])
            for x in range(len(self.board[y])):
                newBoard[y].append(self.getNextState(x, y))
                
        self.board=newBoard
        self.increaseSize()
    

    # increase the size of the board
    def increaseSize(self):
        if 1 in self.board[0]:
            self.board.insert(0, [])
            for x in range(len(self.board[1])):
                self.board[0].append(0)

        if 1 in self.board[-1]:
            self.board.append([])
            for x in range(len(self.board[0])):
                self.board[-1].append(0)

        for row in self.board:
            if row[0]==1:
                for dRow in range(len(self.board)):
                    self.board[dRow].insert(0, 0)
                break     

        for row in self.board:
            if row[-1]==1:
                for dRow in range(len(self.board)):
                    self.board[dRow].append(0)
                break               


    # Return a printable form of the board attribute
    def __str__(self) -> str:
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

    board=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    game=Life(board)
    while True:
        os.system('cls')
        print(game)
        game.nextTurn()
        time.sleep(DELAY)

