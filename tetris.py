import sys
import random

import pygame

import board_class
import graphics

def generate_new_block(board):
    #piece_types = ["STRAIGHT", "S", "Z", "L", "J", "SQUARE", "T"]
    piece_types = ["STRAIGHT", "SQUARE"]
    new_piece_type = random.choice(piece_types)
    new_piece_pos = calc_new_piece_pos(new_piece_type, board)
    board.add_piece(new_piece_pos)


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
