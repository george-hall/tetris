import sys
import random

import pygame

from colour_defs import *

pygame.init()
NUM_ROWS = 40
NUM_COLS = 10

SQUARE_WIDTH = 10
SQUARE_HEIGHT = 10
MARGIN = 1
SIZE = [(NUM_COLS * SQUARE_WIDTH) + ((NUM_COLS + 1) * MARGIN), (NUM_ROWS * SQUARE_HEIGHT) + ((NUM_ROWS + 1) * MARGIN)]
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw grid:
    SCREEN.fill(BLACK)
    for x in xrange(0, NUM_ROWS):
        for y in xrange(0, NUM_ROWS):
            pygame.draw.rect(SCREEN, WHITE, [((MARGIN + SQUARE_WIDTH) * x) + MARGIN, ((MARGIN + SQUARE_HEIGHT) * y) + MARGIN, SQUARE_WIDTH, SQUARE_HEIGHT])

    pygame.display.update()
    clock.tick(10)
