from typing import Final
from enum import Enum

BASE_COLOR: Final = "#302f2f"
MARGIN_COLOR: Final = "#020c18"

class Bag(Enum):
    O = 0
    I = 1
    J = 2
    L = 3
    S = 4
    Z = 5
    T = 6

class Block(object): 
    def __init__(self, row, col):
        self.relCoords = (row, col)
        self.isOccupied = False
        self.color = BASE_COLOR

class Tetromino(object):
    def __init__(self):
        self.currentState = 0
        self.prevState = 0
        self.absCoords = (0, 0)
        self.states = [[Block(0,0), Block(0,0), Block(0,0), Block(0,0)] * 4]
        self.color = BASE_COLOR
        self.shape = "Null"
    
class O(Tetromino):
    def __init__(self):
        super(O, self).__init__()
        
        # Does not rotate at all in SRS           ##
        # Offset is based on bottom left block -> ##
        self.states = [
            [Block(0, 0), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing up
            [Block(0, 0), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing right
            [Block(0, 0), Block(-1, 0), Block(0, 1), Block(-1, 1)], # Facing down
            [Block(0, 0), Block(-1, 0), Block(0, 1), Block(-1, 1)]  # Facing left
        ]
        self.color = "#ffff00"
        self.shape = "O"

class I(Tetromino):
    def __init__(self):
        super(I, self).__init__()
        
        # Offset is based on middle left block ####
        #                                       ^
        self.states = [
            [Block(0, 0), Block(0, -1), Block(0, 1), Block(0, 2)], # Facing up
            [Block(0, 0), Block(-1, 0), Block(1, 0), Block(2, 0)], # Facing right
            [Block(0, 0), Block(0, 1), Block(0, -1), Block(0, -2)], # Facing down
            [Block(0, 0), Block(-1, 0), Block(1, 0), Block(2, 0)] # Facing left
        ]
        self.color = "#00ffff"
        self.shape = "I"

class J(Tetromino):
    def __init__(self):
        super(J, self).__init__()
        
        #                                        #
        # Offset is based on bottom middle block ###
        #                                         ^
        self.states = [
            [Block(0, 0), Block(0, 1), Block(0, -1), Block(-1, -1)], # Facing up
            [Block(0, 0), Block(-1, 0), Block(-1, 1), Block(1, 0)], # Facing right
            [Block(0, 0), Block(0, 1), Block(0, -1), Block(1, 1)], # Facing down
            [Block(0, 0), Block(-1, 0), Block(1, 0), Block(1, -1)] # Facing left
        ]
        self.color = "#0000ff"
        self.shape = "J"
        
class L(Tetromino):
    def __init__(self):
        super(L, self).__init__()
        
        #                                          #
        # Offset is based on bottom middle block ###
        #                                         ^
        self.states = [
            [Block(0, 0), Block(0, 1), Block(-1, 1), Block(0, -1)], # Facing up
            [Block(0, 0), Block(-1, 0), Block(1, 1), Block(1, 0)], # Facing right
            [Block(0, 0), Block(0, 1), Block(0, -1), Block(1, -1)], # Facing down
            [Block(0, 0), Block(-1, 0), Block(1, 0), Block(-1, -1)] # Facing left
        ]
        self.color = "#ffaa00"
        self.shape = "L"
        
class S(Tetromino):
    def __init__(self):
        super(S, self).__init__()
        
        #                                         ##
        # Offset is based on bottom middle block ##
        #                                         ^
        self.states = [
            [Block(0, 0), Block(-1, 0), Block(-1, 1), Block(0, -1)], # Facing up
            [Block(0, 0), Block(-1, 0), Block(0, 1), Block(1, 1)], # Facing right
            [Block(0, 0), Block(0, 1), Block(1, 0), Block(1, -1)], # Facing down
            [Block(0, 0), Block(0, -1), Block(1, 0), Block(-1, -1)] # Facing left
        ]
        self.color = "#00ff00"
        self.shape = "S"
        
class Z(Tetromino):
    def __init__(self):
        super(Z, self).__init__()
        
        #                                        ##
        # Offset is based on bottom middle block  ##
        #                                         ^
        self.states = [
            [Block(0, 0), Block(-1, 0), Block(-1, -1), Block(0, 1)], # Facing up
            [Block(0, 0), Block(0, 1), Block(-1, 1), Block(1, 0)], # Facing right
            [Block(0, 0), Block(0, -1), Block(1, 0), Block(1, 1)], # Facing down
            [Block(0, 0), Block(0, -1), Block(-1, 0), Block(1, -1)] # Facing left
        ]
        self.color = "#ff0000"
        self.shape = "Z"

class T(Tetromino):
    def __init__(self):
        super(T, self).__init__()
        
        #                                            #
        # Offset is based on bottom middle block    ###
        #                                            ^
        self.states = [
            [Block(0, 0), Block(-1, 0), Block(0, -1), Block(0, 1)], # Facing up
            [Block(0, 0), Block(1, 0), Block(-1, 0), Block(0, 1)],  # Facing right
            [Block(0, 0), Block(0, 1), Block(0, -1), Block(1, 0)],  # Facing down
            [Block(0, 0), Block(-1, 0), Block(1, 0), Block(0, -1)]  # Facing left
        ]
        self.color = "#9900ff"
        self.shape = "T"
        
