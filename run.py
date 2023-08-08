import random

# Function to initialize the game boards
def initialize_board(grid_size):
    return [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Function to print the game boards
def print_boards(player_board, cpu_board, grid_size, hide_cpu_ships=True):
    col_labels = " ".join(chr(65 + i) for i in range(grid_size))
    print(f"{username} Board:          CPU Board:")
    print("   " + col_labels + "      " + "   " + col_labels)
    for i in range(grid_size):
        if hide_cpu_ships:
            cpu_row = ["." if cell == 'S' else cell for cell in cpu_board[i]]
        else:
            cpu_row = cpu_board[i]
        row_str = str(i) + "  " + " ".join(player_board[i]) + "   " + str(i) + "  " + " ".join(computer_row)
        print(row_str)
