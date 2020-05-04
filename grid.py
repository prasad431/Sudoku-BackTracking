import pygame
import time
from random_attributes import Attributes
from validator import *
from Cube import *

pygame.font.init()
attributes = Attributes()
font_color = attributes.randomcolor_generator()
temp_color = attributes.randomcolor_generator()
font_name = attributes.randomfont_selection()
timer_color = attributes.randomcolor_generator()
sudoku = attributes.random_board()

class Grid:
    board = sudoku
    def __init__(self, r, c, w, h, window):
        self.rows = r
        self.cols = c
        self.cubes = [[Cube(self.board[i][j], i, j, w, h) for j in range(c)] for i in range(r)]
        self.width = w
        self.height = h
        self.model = None
        self.update_model()
        self.selected = None
        self.win = window

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row,col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, v):
        r, c = self.selected
        self.cubes[r][c].set_temp(v)

    def draw(self):
        # Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    """
    :param: pos
    :return: (row, col)
    """
    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

    def solve(self):
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i

                if self.solve():
                    return True

                self.model[row][col] = 0

        return False

    def solve_gui(self):
        f = find_empty(self.model)
        if not f:
            return True
        else:
            r, c = f

        for i in range(1, 10):
            if valid(self.model, i, (r, c)):
                self.model[r][c] = i
                self.cubes[r][c].set(i)
                self.cubes[r][c].draw_change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(100)

                if self.solve_gui():
                    return True

                self.model[r][c] = 0
                self.cubes[r][c].set(0)
                self.update_model()
                self.cubes[r][c].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False
