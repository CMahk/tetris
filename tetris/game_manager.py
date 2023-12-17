from sre_parse import State
from typing import Final
from tetrominos import *
import random

# In pixels
BLOCK_SIZE: Final = 25

EMPTY_BLOCK: Final = Block(0,0)

# In blocks
BOARD_WIDTH: Final = 10 
BOARD_HEIGHT: Final = 23

# Starting coordinate for tetrominos
STARTING_COORD_ROW: Final = 19
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

    def tick(self):
        self.__drop()
        self.__updateBoard()
        
    def __drop(self):
        # Attempt to drop the current tetromino down by 1 row
        self.currentMino.prevAbsCoords = self.currentMino.absCoords
        absCoords = self.getAbsoluteCoords() # Get all coordinates of the current tetromino

        # Ensure that the current mino won't collide with anything present
        checks = [False, False, False, False]
        
        for i in range(0, 4):
            row, col = absCoords[i]
            checkRow = row + 1
            if (checkRow < BOARD_HEIGHT): # Make sure the desired move isn't past the board wall
                if (not self.board.blockGrid[checkRow][col].isOccupied):
                    checks[i] = True
                elif ((checkRow, col) in absCoords): # The block is occupied, but is it because it's part of the current mino?
                    checks[i] = True # If so, we're safe  
                
        # If all True, then we're good to drop 1 row
        if (all(checks)):
            row, col = self.currentMino.absCoords
            self.currentMino.absCoords = (row + 1, col)

    def __updateBoard(self):
        # Remove previous state blocks

        # State AND coords changed
        if ((self.currentMino.prevState != self.currentMino.currentState) and (self.currentMino.prevAbsCoords != self.currentMino.absCoords)):
                for block in self.currentMino.getStates()[self.currentMino.prevState]:
                    relRow, relCol = block.relCoords
                    absRow, absCol = self.currentMino.prevAbsCoords
                    self.board.blockGrid[absRow + relRow][absCol + relCol] = EMPTY_BLOCK
        else: # Otherwise one or the other?
            # Tetromino rotated?
            if (self.currentMino.prevState != self.currentMino.currentState):
                for block in self.currentMino.getStates()[self.currentMino.prevState]:
                    relRow, relCol = block.relCoords
                    absRow, absCol = self.currentMino.absCoords
                    self.board.blockGrid[absRow + relRow][absCol + relCol] = EMPTY_BLOCK
            # Coordinates changed?
            if (self.currentMino.prevAbsCoords != self.currentMino.absCoords):
                for block in self.currentMino.getStates()[self.currentMino.currentState]:
                    relRow, relCol = block.relCoords
                    absRow, absCol = self.currentMino.prevAbsCoords
                    self.board.blockGrid[absRow + relRow][absCol + relCol] = EMPTY_BLOCK

        # Update current state blocks
        for block in self.currentMino.getStates()[self.currentMino.currentState]:
            relRow, relCol = block.relCoords
            absRow, absCol = self.currentMino.absCoords
            self.board.blockGrid[absRow + relRow][absCol + relCol] = block

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
        
    def getAbsoluteCoords(self):
        absCoords = [(0,0), (0,0), (0,0), (0,0)]
        
        # 4 blocks in a given state
        state = self.currentMino.getStates()[self.currentMino.currentState]
        for i in range(0, 4):
            absRow, absCol = self.currentMino.absCoords
            relRow, relCol = state[i].relCoords
            absCoords[i] = (absRow + relRow, absCol + relCol)
                
        return absCoords
    
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
        self.currentMino.prevAbsCoords = self.currentMino.absCoords
        absCoords = self.getAbsoluteCoords() # Get all coordinates of the current tetromino

        # Ensure that the current mino won't collide with anything present
        checks = [False, False, False, False]
        
        for i in range(0, 4):
            row, col = absCoords[i]
            checkCol = col - 1
            if (checkCol >= 0): # Make sure the desired move isn't past the board wall
                if (not self.board.blockGrid[row][checkCol].isOccupied):
                    checks[i] = True
                elif ((row, checkCol) in absCoords): # The block is occupied, but is it because it's part of the current mino?
                    checks[i] = True # If so, we're safe
                    
        # If all True, then we're good to move left
        if (all(checks)):
            row, col = self.currentMino.absCoords
            self.currentMino.absCoords = (row, col - 1)
            
        self.__updateBoard()
        
    def moveRight(self):
        self.currentMino.prevAbsCoords = self.currentMino.absCoords
        absCoords = self.getAbsoluteCoords() # Get all coordinates of the current tetromino

        # Ensure that the current mino won't collide with anything present
        checks = [False, False, False, False]
        
        for i in range(0, 4):
            row, col = absCoords[i]
            checkCol = col + 1
            if (checkCol < BOARD_WIDTH): # Make sure the desired move isn't past the board wall
                if (not self.board.blockGrid[row][checkCol].isOccupied):
                    checks[i] = True
                elif ((row, checkCol) in absCoords): # The block is occupied, but is it because it's part of the current mino?
                    checks[i] = True # If so, we're safe  
                
                    
        # If all True, then we're good to move right
        if (all(checks)):
            row, col = self.currentMino.absCoords
            self.currentMino.absCoords = (row, col + 1)
        
        self.__updateBoard()
        
    def hold(self):
        print("TODO: hold")
        