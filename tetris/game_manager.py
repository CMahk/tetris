from typing import Final
from tetrominos import *
import random

# In pixels
BLOCK_SIZE: Final = 25

# In blocks
BOARD_WIDTH: Final = 10 
BOARD_HEIGHT: Final = 23

# Starting coordinate for tetrominos
STARTING_COORD_ROW: Final = 1
STARTING_COORD_COL: Final = 4

class Board(object):
    def __init__(self):
        # Create an empty board of Block objects
        self.blockGrid = [[Block(0, 0) for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)] 
    
class GameManager(object):
    def __init__(self):
        self.board = Board()
        self.currentBag = self.__createBag()
        self.nextBag = self.__createBag()
        self.nextTetromino()
        
    def __updateBoard(self):
        # Remove previous state blocks
        if (self.currentMino.prevState != self.currentMino.currentState):
            for block in self.currentMino.states[self.currentMino.prevState]:
                relRow, relCol = block.relCoords
                absRow, absCol = self.currentMino.absCoords
                self.board.blockGrid[absRow + relRow][absCol + relCol].color = BASE_COLOR
                self.board.blockGrid[absRow + relRow][absCol + relCol].isOccupied = False

        # Update current state blocks
        for block in self.currentMino.states[self.currentMino.currentState]:
            relRow, relCol = block.relCoords
            absRow, absCol = self.currentMino.absCoords
            self.board.blockGrid[absRow + relRow][absCol + relCol].color = self.currentMino.color
            self.board.blockGrid[absRow + relRow][absCol + relCol].isOccupied = True

    def __updateMinoState(self, inc):
        # Update state so game board knows what to refresh
        self.currentMino.prevState = self.currentMino.currentState
        
        self.currentMino.currentState += inc
        if (self.currentMino.currentState == 4): # Wrap 4 around to 0
            self.currentMino.currentState = 0
        if (self.currentMino.currentState == 5): # Wrap 3 around to 1 (mino was reversed)
            self.currentMino.currentState = 1
        elif (self.currentMino.currentState == -1): # Wrap -1 around to 3
            self.currentMino.currentState = 3
            
    def __createBag(self):
        bag = [Bag.O, Bag.I, Bag.J, Bag.L, Bag.S, Bag.Z, Bag.T]
        random.shuffle(bag)
        return bag

    def __EnumToMino(self, enum):
        if (enum.value == 0):
            return O()
        elif (enum.value == 1):
            return I()
        elif (enum.value == 2):
            return J()
        elif (enum.value == 3):
            return L()
        elif (enum.value == 4):
            return S()
        elif (enum.value == 5):
            return Z()
        elif (enum.value == 6):
            return T()

    def nextTetromino(self):
        self.currentMino = self.__EnumToMino(self.currentBag[0])
        del self.currentBag[0]
        
        if (len(self.currentBag) == 0):
            self.currentBag = self.nextBag
            self.nextBag = self.__createBag()
        
        self.currentMino.absCoords = (STARTING_COORD_ROW, STARTING_COORD_COL)
        self.__updateBoard()
    
    def cw(self):
        self.__updateMinoState(1)
        self.__updateBoard()

    def ccw(self):
        self.__updateMinoState(-1)
        self.__updateBoard()
        
    def reverse(self):
        self.__updateMinoState(2)
        self.__updateBoard()

    def softDrop(self):
        print("TODO: soft drop")
        
    def hardDrop(self):
        print("TODO: hard drop")
        
    def moveLeft(self):
        print("TODO: move left")
        
    def moveRight(self):
        print("TODO: move right")
        
    def hold(self):
        print("TODO: hold")
        