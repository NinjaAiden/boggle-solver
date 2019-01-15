from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Create a grid that will hold all the tiles
    for a Boggle game
    """
    
    if width != 0 or height != 0:
        return {(row, col): choice(ascii_uppercase)
            for row in range(height)
            for col in range(width)
        }
    else:
        return {}