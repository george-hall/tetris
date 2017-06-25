import sys

import pygame

from colour_defs import *

def draw_square(screen, board, (x, y), colour):
    pygame.draw.rect(screen, colour, \
                     [((board.margin + board.square_width) * x) + board.margin, \
                     ((board.margin + board.square_height) * y) + board.margin, \
                     board.square_width, board.square_height])


def draw_piece(screen, board, piece):
    colour = piece.colour
    for (x,y) in piece.positions:
        draw_square(screen, board, (x,y), colour)


def draw_screen(screen, board):
    screen.fill(BLACK)
    for x in xrange(0, board.num_cols):
        for y in xrange(0, board.num_rows):
            draw_square(screen, board, x, y)
