import tkinter as tk
from game_manager import *
from timer import *
from typing import Final

# In pixels
CANVAS_WIDTH: Final  = BLOCK_SIZE * BOARD_WIDTH
CANVAS_HEIGHT: Final = BLOCK_SIZE * BOARD_HEIGHT

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(str(CANVAS_WIDTH + 100) + "x" + str(CANVAS_HEIGHT + 100)) # Width x Height
        self.title("Tetris")
        self.resizable(False, False)
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Grid for window (Is this needed?)
        for x in range(0, 3):
            self.columnconfigure(x, weight = 1)
        for y in range(0, 3):
            self.rowconfigure(y, weight = 1)
            
        # Create the game manager and canvas
        self.gm = GameManager()

        self.canvas = GameCanvas(self)
        self.canvas.pack(padx = 50, pady = 50)
        
        # Game timer
        self.timer = RepeatedTimer(1.0, self.__tick)

        # Keyboard input
        self.bind("<Key>", self.__keyEventListener)
        
        self.__updateWindow()
        
    def __tick(self):
        self.gm.tick()
        self.__updateWindow()

    def __updateWindow(self):
        mino = self.gm.currentMino
        
        # if (mino.prevState != mino.currentState):
        #     for block in mino.states[mino.prevState]:
        #         relRow, relCol = block.relCoords
        #         absRow, absCol = mino.absCoords
        #         if ((absRow + relRow) <= 2):
        #             self.canvas.frameGrid[absRow + relRow][absCol + relCol].config(bg = MARGIN_COLOR)
        #         else:
        #             self.canvas.frameGrid[absRow + relRow][absCol + relCol].config(bg = BASE_COLOR)

        # Update current state blocks
        for row in range(0, BOARD_HEIGHT):
            for col in range(0, BOARD_WIDTH):
                self.canvas.frameGrid[row][col].config(bg = self.gm.board.blockGrid[row][col].getColor())

    def __keyEventListener(self, event):
        if (event.keysym == "Up" or event.keysym == "x"):
            self.gm.cw()
        elif (event.keysym == "z" or event.keysym == "Control_L"):
            self.gm.ccw()
        elif (event.keysym == "a"):
            self.gm.reverse()
        elif (event.keysym == "Down"):
            self.gm.softDrop()
        elif (event.keysym == "Left"):
            self.gm.moveLeft()
        elif (event.keysym == "Right"):
            self.gm.moveRight()
        elif (event.keysym == "c" or event.keysym == "Shift_L"):
            self.gm.hold()
        elif (event.keysym == "space"):
            self.gm.hardDrop()
            
        self.__updateWindow()

class GameCanvas(tk.Canvas):
    def __init__(self, window):
        super().__init__()
        self.master = window
        self.configure(
            width = BOARD_WIDTH * BLOCK_SIZE,
            height = BOARD_HEIGHT * BLOCK_SIZE,
            bg = "firebrick1"
        )
        
        # Visualize the block grid via frames
        self.frameGrid = [[tk.Frame() for row in range(BOARD_WIDTH)] for col in range(BOARD_HEIGHT)] 
       
        # Create grid managers for the board
        for col in range(0, BOARD_WIDTH):
            self.columnconfigure(col, weight = 1)
        for row in range(0, BOARD_HEIGHT):
            self.rowconfigure(row, weight = 1)
        
        # Upper 3 rows should be blank
        for y in range(0, 3):
            for x in range(0, BOARD_WIDTH):
                frame = tk.Frame(
                    self,
                    bg=MARGIN_COLOR,
                    width = BLOCK_SIZE,
                    height = BLOCK_SIZE,
                    relief = tk.SOLID,
                    borderwidth = 1
                )
                frame.grid(row = y, column = x)
                self.frameGrid[y][x] = frame

        # Main board blocks
        for y in range(3, BOARD_HEIGHT):
            for x in range(0, BOARD_WIDTH):
                frame = tk.Frame(
                    self,
                    bg=window.gm.board.blockGrid[y][x].getColor(),
                    width = BLOCK_SIZE,
                    height = BLOCK_SIZE,
                    relief = tk.SOLID,
                    borderwidth = 1
                )
                frame.grid(row = y, column = x)
                self.frameGrid[y][x] = frame
        
#if __name__ == "__main__":
gw = GameWindow()
gw.mainloop()
