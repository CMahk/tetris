from typing import Final
from enum import Enum

BASE_COLOR: Final = "#302f2f"
MARGIN_COLOR: Final = "#020c18"
TEST_COLOR: Final = "#bbbbbb"

class Bag(Enum):
    O = 0
    I = 1
    J = 2
    L = 3
    S = 4
    Z = 5
    T = 6

class Block(object): 
    def __init__(self, row = 0, col = 0):
        self.relCoords = (row, col)
        self.isOccupied = False
        self.isCurrent = False
        self.isPlaced = False
        self._color = BASE_COLOR
        
    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color = color

class Tetromino(object):
    # Tetromino is created. We can assume it is the current piece the player is using
    # The fields are set via the child's __init__()
    def __init__(self):
        self.currentState = 0
        self.prevState = 0
        self.absCoords = (0, 0)
        self.prevAbsCoords = (0, 0)
        self._states = [[Block(), Block(), Block(), Block()] * 4]
        self.shape = "Null"
        
    def _setColor(self, color):
        for state in self._states:
            for block in state:
                block.setColor(color)
             
    def _setStates(self, states):
        self._states = states
                
    def getStates(self):
        return self._states

    def getStateBlocks(self, desiredState):
        return self.getStates()[desiredState]

    def updateCurrentBlockState(self):
        # Set all states to False
        for state in self._states:
            for block in state:
                block.isCurrent = False
                block.isOccupied = False

        # Only set the current state to True
        for block in self.getStateBlocks(self.currentState):
            block.isCurrent = True
            block.isOccupied = True
    
    def tetrominoPlaced(self):
        self.updateCurrentBlockState()        

        for block in self.getStateBlocks(self.currentState):
            block.isCurrent = False
            block.isOccupied = True
            block.isPlaced = True
            
    
class O(Tetromino):
    def __init__(self):
        super(O, self).__init__()
        
        # Does not rotate at all in SRS           ##
        # Offset is based on bottom left block -> ##
        self._setStates([
            [Block(), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing up
            [Block(), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing right
            [Block(), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing down
            [Block(), Block(-1, 0), Block(0, 1), Block(-1, 1)]  # Facing left
        ])
        self._setColor("#ffff00")
        self.updateCurrentBlockState()
        self.shape = "O"

class I(Tetromino):
    def __init__(self):
        super(I, self).__init__()
        
        # Offset is based on middle left block ####
        #                                       ^
        self._setStates([
            [Block(), Block(0, -1), Block(0, 1), Block(0, 2)], # Facing up
            [Block(), Block(-1, 0), Block(1, 0), Block(2, 0)], # Facing right
            [Block(), Block(0, 1), Block(0, -1), Block(0, -2)], # Facing down
            [Block(), Block(-1, 0), Block(1, 0), Block(2, 0)] # Facing left
        ])
        self._setColor("#00ffff")
        self.updateCurrentBlockState()
        self.shape = "I"

class J(Tetromino):
    def __init__(self):
        super(J, self).__init__()
        
        #                                        #
        # Offset is based on bottom middle block ###
        #                                         ^
        self._setStates([
            [Block(), Block(0, 1), Block(0, -1), Block(-1, -1)], # Facing up
            [Block(), Block(-1, 0), Block(-1, 1), Block(1, 0)], # Facing right
            [Block(), Block(0, 1), Block(0, -1), Block(1, 1)], # Facing down
            [Block(), Block(-1, 0), Block(1, 0), Block(1, -1)] # Facing left
        ])
        self._setColor("#0000ff")
        self.updateCurrentBlockState()
        self.shape = "J"
        
class L(Tetromino):
    def __init__(self):
        super(L, self).__init__()
        
        #                                          #
        # Offset is based on bottom middle block ###
        #                                         ^
        self._setStates([
            [Block(), Block(0, 1), Block(-1, 1), Block(0, -1)], # Facing up
            [Block(), Block(-1, 0), Block(1, 1), Block(1, 0)], # Facing right
            [Block(), Block(0, 1), Block(0, -1), Block(1, -1)], # Facing down
            [Block(), Block(-1, 0), Block(1, 0), Block(-1, -1)] # Facing left
        ])
        self._setColor("#ffaa00")
        self.updateCurrentBlockState()
        self.shape = "L"
        
class S(Tetromino):
    def __init__(self):
        super(S, self).__init__()
        
        #                                         ##
        # Offset is based on bottom middle block ##
        #                                         ^
        self._setStates([
            [Block(), Block(-1, 0), Block(-1, 1), Block(0, -1)], # Facing up
            [Block(), Block(-1, 0), Block(0, 1), Block(1, 1)], # Facing right
            [Block(), Block(0, 1), Block(1, 0), Block(1, -1)], # Facing down
            [Block(), Block(0, -1), Block(1, 0), Block(-1, -1)] # Facing left
        ])
        self._setColor("#00ff00")
        self.updateCurrentBlockState()
        self.shape = "S"
        
class Z(Tetromino):
    def __init__(self):
        super(Z, self).__init__()
        
        #                                        ##
        # Offset is based on bottom middle block  ##
        #                                         ^
        self._setStates([
            [Block(), Block(-1, 0), Block(-1, -1), Block(0, 1)], # Facing up
            [Block(), Block(0, 1), Block(-1, 1), Block(1, 0)], # Facing right
            [Block(), Block(0, -1), Block(1, 0), Block(1, 1)], # Facing down
            [Block(), Block(0, -1), Block(-1, 0), Block(1, -1)] # Facing left
        ])
        self._setColor("#ff0000")
        self.updateCurrentBlockState()
        self.shape = "Z"

class T(Tetromino):
    def __init__(self):
        super(T, self).__init__()
        
        #                                            #
        # Offset is based on bottom middle block    ###
        #                                            ^
        self._setStates([
            [Block(), Block(-1, 0), Block(0, -1), Block(0, 1)], # Facing up
            [Block(), Block(1, 0), Block(-1, 0), Block(0, 1)],  # Facing right
            [Block(), Block(0, 1), Block(0, -1), Block(1, 0)],  # Facing down
            [Block(), Block(-1, 0), Block(1, 0), Block(0, -1)]  # Facing left
        ])
        self._setColor("#9900ff")
        self.updateCurrentBlockState()
        self.shape = "T"
        
