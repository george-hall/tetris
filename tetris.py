import sys
import random

import pygame

import board_class
import graphics


def blank_left(piece, board):
    if any(p[0] == 0 for p in piece.positions):
        return False
    for pos in piece.positions:
        if (pos[0] - 1) not in [p[0] for p in piece.positions]:
            if board.cells[pos[0]-1][pos[1]] == 1:
                return False

    return True

def blank_right(piece, board):
    max_col_num = board.num_cols - 1
    if any(p[0] == max_col_num for p in piece.positions):
        return False
    for pos in piece.positions:
        if (pos[0] + 1) not in [p[0] for p in piece.positions]:
            if board.cells[pos[0]+1][pos[1]] == 1:
                return False

    return True


def blank_below(piece, board):
    if piece_at_bottom(piece, board):
        return False

    for pos in piece.positions:
        # Check that the position being examined does not have another position
        # from the same piece directly below
        if (pos[1] + 1) not in [p[1] for p in piece.positions]:
            if board.cells[pos[0]][pos[1]+1] == 1:
                return False
    return True


def piece_at_bottom(piece, board):
    bottom_row = board.num_rows - 1
    if any(pos[1] == bottom_row for pos in piece.positions):
        return True

    return False


def move_blocks_down(board):
    blocks_moved = False
    for piece in board.pieces:
        if blank_below(piece, board):
            new_piece_positions = [(p[0],p[1]+1) for p in piece.positions]
            piece.positions = new_piece_positions
            blocks_moved = True

    board.update_cells()

    return blocks_moved


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
            if event.type == pygame.KEYDOWN:
                # Active piece is most recent piece added and the one of which
                # the player is in control
                active_piece = board.pieces[-1]
                if event.key == pygame.K_LEFT:
                    if blank_left(active_piece, board):
                        active_piece.move_left()
                elif event.key == pygame.K_RIGHT:
                    if blank_right(active_piece, board):
                        active_piece.move_right()
                board.update_cells()



        if blocks_moved == False:
            generate_new_block(board)

        blocks_moved = move_blocks_down(board)

        graphics.draw_screen(screen, board)
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
