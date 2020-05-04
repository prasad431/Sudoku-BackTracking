import pygame
import time
from random_attributes import Attributes
from grid import *
from Cube import *
from validator import *

pygame.font.init()
attributes = Attributes()
font_name = attributes.randomfont_selection()
timer_color = attributes.randomcolor_generator()

def draw_window(window, board, time, worng_strikes):
    window.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont(font_name, 30)
    text = fnt.render("Time: " + time_format(time), 1, timer_color)
    window.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * worng_strikes, 1, (255, 0, 0))
    window.blit(text, (20, 560))
    # Draw grid and board
    board.draw()


def time_format(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def agent():
    window = pygame.display.set_mode((550,600))
    pygame.display.set_caption("Sudoku")
    bo = Grid(9, 9, 540, 540, window)
    key = None
    run = True
    start_time = time.time()
    worng_strikes = 0
    while run:

        pl_time = round(time.time() - start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = bo.click(pos)
                if bo.click(pos):
                    bo.select(clicked[0], clicked[1])
                    key = None

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DELETE:
                    bo.clear()
                    key = None

                if event.key == pygame.K_SPACE:
                    bo.solve_gui()

                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_RETURN:
                    i, j = bo.selected
                    if bo.cubes[i][j].temp != 0:
                        if bo.place(bo.cubes[i][j].temp):
                            print("Correct Number")
                        else:
                            print("Wrong Number")
                            worng_strikes += 1
                        key = None

                        if bo.is_finished():
                            print("Game over")

        if bo.selected and key != None:
            bo.sketch(key)

        draw_window(window, bo, pl_time, worng_strikes)
        pygame.display.update()


if __name__ == '__main__':
    agent()
    pygame.quit()
