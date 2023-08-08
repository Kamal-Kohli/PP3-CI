import random

# Function to initialize the game boards
def initialize_board(grid_size):
    return [['.' for _ in range(grid_size)] for _ in range(grid_size)]