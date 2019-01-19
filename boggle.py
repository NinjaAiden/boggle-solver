from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Create a grid that will hold all the tiles
    for a Boggle game
    """
    
    # check for valid grid size and populate with letters
    if width != 0 or height != 0:
        return {(row, col): choice(ascii_uppercase)
            for row in range(height)
            for col in range(width)
        }
    else:
        return {}

def neighbours_of_position(coords):
    """
    get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    # assign each of the neighbours
    
    # top left to top right
    top_left = (row -1, col -1)
    top_center = (row -1, col)
    top_right = (row -1, col +1)
    
    # left to right
    center_left = (row, col -1)
    # center is current tile and is not necessary to check
    center_right = (row, col +1)
    
    # bottom right to bottom left
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_center, top_right,
            center_left, center_right,
            bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    get all possible neighbour positions for each position in the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    """
    add all of the letters on a path to a string
    """
    return ''.join([grid[p] for p in path])

def word_in_dictionary(word, dict):
    return word in dict

def search(grid, dictionary):
    """
    search through paths to locate words by matching strings
    to words in a dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
    
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

def get_dictionary(dictionary_file):
    """
    load dictionary file
    """
    full_words, stems = set(), set()
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
        
    return full_words, stems

def display_words(words):
    """
    prints out list of words and total number of words found
    """
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    """
    this is the function that will run the whole project
    """
    grid = make_grid(3, 3)
    dictionary = get_dictionary('words.txt')
    words = search(grid, dictionary)
    display_words(words)

if __name__ == "__main__":
    main()