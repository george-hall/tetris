BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

def calc_colour(piece_type):
    if piece_type == "STRAIGHT":
        return CYAN
    elif piece_type == "SQUARE":
        return YELLOW
