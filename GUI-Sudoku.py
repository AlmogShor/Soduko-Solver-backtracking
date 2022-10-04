import pygame as pg

import time

# Colors for the GUI
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Window size of the GUI
WIDTH = 570
HEIGHT = 600
BOTTOM = 50  # Bottom margin of the window for time and difficulty
THICK_LINE = 6  # Thickness of the thick lines
THIN_LINE = 2  # Thickness of the thin lines
FPS = 60  # Frames per second
### Box_size = (Width-4*Thick_line - 6*THIN_LINE)/9


# game initialization and configuration
pg.init()
pg.font.init()
pg.display.set_caption("Sudoku")
WIN = pg.display.set_mode((WIDTH, HEIGHT + BOTTOM))  # Window
clock = pg.time.Clock()


class Grid:

    def __init__(self, rows, cols, board, screen):
        self.game = board
        self.rows = rows
        self.cols = cols
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = screen
        self.solved = False
        '''
         self.lost = False
         self.lives = 7
        '''

        self.difficulty = None
        self.selected_cell = None

    def place(self):
        '''Method to update the board with a new number'''

        if self.selected_cell:
            row, col = self.selected_cell


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height, screen):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.screen = screen
        self.is_selected = False

    def draw(self, window):
        fnt = pg.font.SysFont("comicsans", 40) \
 \
        gap = self.width / 9  # Gap between each cell
        x_pos = self.col * gap  # X position of the cell
        y_pos = self.row * gap

        if self.temp != 0 and self.value == 0:
            txt = fnt.render(str(self.temp), 2, GREY)
            window.blit(txt, (x_pos + 5, y_pos + 5))


class Button:
