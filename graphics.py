import sys

import pygame

from colour_defs import *

def draw_square(screen, board, x, y):
    pygame.draw.rect(screen, WHITE, \
                     [((board.margin + board.square_width) * x) + board.margin, \
                     ((board.margin + board.square_height) * y) + board.margin, \
                     board.square_width, board.square_height])


def draw_screen(screen, board):
    screen.fill(BLACK)
    for x in xrange(0, board.num_rows):
        for y in xrange(0, board.num_rows):
            draw_square(screen, board, x, y)
