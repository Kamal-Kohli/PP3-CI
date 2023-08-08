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

# Function to place ships on the board
def place_ship(board, ship_size):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board[0]) - ship_size)
            if all(board[x][y+i] == '.' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x][y+i] = 'S'
                break
        else:
            x = random.randint(0, len(board) - ship_size)
            y = random.randint(0, len(board[0]) - 1)
            if all(board[x+i][y] == '.' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x+i][y] = 'S'
                break

# Function to play the Battleship game
def play_battleship(grid_size, username):
    player_board = initialize_board(grid_size)
    cpu_board = initialize_board(grid_size)

    ships = [5, 4, 3, 3, 2]
    for ship_size in ships:
        place_ship(player_board, ship_size)
        place_ship(cpu_board, ship_size)

    print(f"Welcome {username} to Battleship!")
    print_boards(player_board, cpu_board, grid_size, hide_cpu_ships=True)

if __name__ == "__main__":
    while True:
        grid_size = int(input("Enter grid size (5-10): "))
        if 5 <= grid_size <= 10:
            username = input("Enter your username: ")
            play_battleship(grid_size, username)
        else:
            print("Invalid grid size. Please enter a value between  5 and 10.")
