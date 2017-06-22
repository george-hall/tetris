import sys
import random

import pygame

import board_class
import graphics


def blank_below(piece, board):
    for pos in piece.positions:
        # Check that the position being examined does not have another position
        # from the same piece directly below
        if (pos[1] + 1) not in [p[1] for p in piece.positions]:
            if board.cells[pos[0]][pos[1]+1] == 1:
                return False
    return True


def move_blocks_down(board):
    blocks_moved = False
    for piece in board.pieces:
        if blank_below(piece, board):
            new_piece_positions = [(p[0],p[1]+1) for p in piece.positions]
            piece.positions = new_piece_positions
            blocks_moved = True

    board.update_cells()

    return (board, blocks_moved)


def calc_new_piece_pos(new_piece_type, board):
    max_col = board.num_rows - 1
    max_row = board.num_cols - 1

    if new_piece_type == "STRAIGHT":
        return [(int(max_row / 2), 0), (int(max_row / 2), 1),
                (int(max_row / 2), 2), (int(max_row / 2), 3)]

    elif new_piece_type == "SQUARE":
        return [(int(max_row / 2), 0), (int(max_row / 2) + 1, 0),
                (int(max_row / 2), 1), (int(max_row / 2) + 1, 1)]


def generate_new_block(board):
    #piece_types = ["STRAIGHT", "S", "Z", "L", "J", "SQUARE", "T"]
    piece_types = ["STRAIGHT", "SQUARE"]
    new_piece_type = random.choice(piece_types)
    new_piece_pos = calc_new_piece_pos(new_piece_type, board)
    board.add_piece(new_piece_pos)


def main():

    pygame.init()

    board = board_class.Board()
    screen = pygame.display.set_mode(board.size)
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    blocks_moved = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if blocks_moved == False:
            generate_new_block(board)

        (board, blocks_moved) = move_blocks_down(board)
        blocks_moved = True

        graphics.draw_screen(screen, board)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
