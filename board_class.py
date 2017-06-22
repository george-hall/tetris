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

    def add_piece(self, positions):
        new_piece = Piece(positions)
        self.pieces.append(new_piece)
        for p in positions:
            self.cells[p[0]][p[1]] = 1

    def update_cells(self):
        self.cells = [[0 for _ in xrange(self.num_rows)] for _ in xrange(self.num_cols)]
        for piece in self.pieces:
            for pos in piece.positions:
                self.cells[pos[0]][pos[1]] = 1


class Piece():

    def __init__(self, positions):
        self.positions = positions

    def move_left(self):
        if not any(p[0] == 0 for p in self.positions):
            new_positions = [(p[0]-1, p[1]) for p in self.positions]
            self.positions = new_positions

    def move_right(self, num_cols):
        max_col_num = num_cols - 1
        if not any(p[0] == max_col_num for p in self.positions):
            new_positions = [(p[0]+1, p[1]) for p in self.positions]
            self.positions = new_positions
