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

class Piece():

    def __init__(self):
        self.positions = []
