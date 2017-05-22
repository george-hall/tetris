import sys
import random

import pygame

import board_class
import graphics

pygame.init()

board = board_class.Board()
screen = pygame.display.set_mode(board.size)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    graphics.draw_screen(screen, board)
    pygame.display.update()
    clock.tick(10)
