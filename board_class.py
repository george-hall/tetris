import colour_defs

class Board():

    def __init__(self):
        self.num_rows = 40
        self.num_cols = 10
        self.pieces = []
        self.cells = [[0 for _ in xrange(self.num_rows)] for _ in xrange(self.num_cols)]

        self.square_width = 10
        self.square_height = 10
        self.margin = 1

        combined_width_cells = self.num_cols * self.square_width
        combined_width_margin = (self.num_cols + 1) * self.margin
        total_self_width = combined_width_cells + combined_width_margin
        
        combined_height_cells = self.num_rows * self.square_height
        combined_height_margin = (self.num_rows + 1) * self.margin
        total_self_height = combined_height_cells + combined_height_margin

        self.size = [total_self_width, total_self_height]

    def add_piece(self, positions, piece_type):
        new_piece = Piece(positions, piece_type)
        self.pieces.append(new_piece)
        for p in positions:
            self.cells[p[0]][p[1]] = 1

    def update_cells(self):
        self.cells = [[0 for _ in xrange(self.num_rows)] for _ in xrange(self.num_cols)]
        for piece in self.pieces:
            for pos in piece.positions:
                self.cells[pos[0]][pos[1]] = 1


class Piece():

    def __init__(self, positions, piece_type):
        self.positions = positions
        self.piece_type = piece_type
        self.colour = colour_defs.calc_colour(self.piece_type)

    def move_left(self):
        new_positions = [(p[0]-1, p[1]) for p in self.positions]
        self.positions = new_positions

    def move_right(self):
        new_positions = [(p[0]+1, p[1]) for p in self.positions]
        self.positions = new_positions
