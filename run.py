"""
Legend:
1. "." = Water or empty space.
2. "s" = Ships, Ship positions.
3. "#" = Water that was shot with bullets, a miss it hit no ship.
4. "x" = Ship Hit!

Battleship:
A. grid = 10x10Custom grids between min 5 to max 10.
B. 5 ships of variable length randomly placed.
C. Every hit and misses shot will be show up in the grid.
D. If all ships are unearthed before using up all bullets, 
    You Win else, You lose.
E. You can choose a row and column such as A1, B1 to indicate where to shoot.
"""

# Constants and globals
EMPTY = ''' . '''
SHIP = ''' S '''
HIT = ''' X  '''
MISS = ''' # '''
GRID_SIZE = ''' Between 5 to 10 '''  
SHIPS = [5, 4, 3, 2, 2]  # Variation sizes of ships
NUM_SHIPS = 5


import random

# Function to initialize the game boards
def initialize_board(grid_size):
    return [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Function to print the game boards
def print_boards(player_board, computer_board, grid_size, hide_computer_ships=True):
    col_labels = " ".join(chr(65 + i) for i in range(grid_size))
    print(f"{username} Board:      CPU Board:")
    print("   " + col_labels + "   " + "   " + col_labels)
    for i in range(grid_size):
        if hide_computer_ships:
            computer_row = ["." if cell == 'S' else cell for cell in computer_board[i]]
        else:
            computer_row = computer_board[i]
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

# Function to check if the game is over
def is_game_over(board):
    return all(all(cell != 'S' for cell in row) for row in board)

# Function to convert player input to board coordinates
def convert_input(input_str, grid_size):
    try:
        letter = input_str[0].upper()
        number = int(input_str[1:])
        if 'A' <= letter <= chr(65 + grid_size - 1) and 0 <= number < grid_size:
            x = ord(letter) - ord('A')
            y = number
            return x, y
        else:
            return None, None
    except (ValueError, IndexError):
        return None, None

# Function for the player's turn
def player_turn(computer_board, grid_size):
    while True:
        player_input = input("Enter target (e.g., A0, B1): ")
        x, y = convert_input(player_input, grid_size)
        if x is not None and y is not None and computer_board[x][y] != 'X' and computer_board[x][y] != '#':
            if computer_board[x][y] == 'S':
                print("Hit!")
                computer_board[x][y] = 'X'
            else:
                print("Miss!")
                computer_board[x][y] = '#'
            break
        else:
            print("Invalid target, try again.")

# Function for the computer's turn
def computer_turn(player_board, grid_size):
    while True:
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        if player_board[x][y] != 'X' and player_board[x][y] != '#':
            if player_board[x][y] == 'S':
                print("CPU hit at", chr(65 + x) + str(y))
                player_board[x][y] = 'X'
            else:
                print("CPU missed at", chr(65 + x) + str(y))
                player_board[x][y] = '#'
            break

# Function to get user feedback
def get_feedback():
    return input("Please provide your feedback on the game: ")

# Function to play the Battleship game
def play_battleship(grid_size, username):
    player_board = initialize_board(grid_size)
    computer_board = initialize_board(grid_size)

    ships = [5, 4, 3, 2, 2]
    for ship_size in ships:
        place_ship(player_board, ship_size)
        place_ship(computer_board, ship_size)

    print(f"Welcome, {username}, to Battleship!")
    print_boards(player_board, computer_board, grid_size, hide_computer_ships=True)

    while True:
        player_turn(computer_board, grid_size)
        print_boards(player_board, computer_board, grid_size, hide_computer_ships=True)
        if is_game_over(computer_board):
            print("Congratulations! You sank all the computer's ships. You win!")
            feedback = get_feedback()
            print("Thank you for playing!")
            break

        computer_turn(player_board, grid_size)
        print_boards(player_board, computer_board, grid_size, hide_computer_ships=True)
        if is_game_over(player_board):
            print("Game over! The computer sank all your ships. You lose!")
            feedback = get_feedback()
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    while True:
        grid_size = int(input("Enter grid size (5-10): "))
        if 5 <= grid_size <= 10:
            username = input("Enter your username: ")
            play_battleship(grid_size, username)
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again == 'no':
                print("Thank you for playing!")
                break
        else:
            print("Invalid grid size. Please enter a value between 5 and 10.")
    main()
