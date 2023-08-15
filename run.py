"""
Legend:
1. "." = Water or empty space.
2. "s" = Ships, Ship positions.
3. "#" = Water shot with bullets, a miss it hit no ship.
4. "x" = Ship Hit!

Battleship:
A. grid = 10x10Custom grids between min 5 to max 10.
B. 5 ships of variable length were randomly placed.
C. Every hit or miss shot will show up in the grid.
D. If all ships are unearthed before using up all bullets,
You Win else, You lose.
E. You can choose a row and column such as A1, B1 to indicate where to shoot.
"""


import random

GAME_INSTRUCTIONS = """
INSTRUCTIONS!!!

1. Enter your grid size.
2. Enter Your Name.
3. Enter your coordinates on the map to sink the enemy's fleet.
e.g. A1, B1

Now you're ready for the Navel war Captain. GOOD LUCK!
"""

# Constants and globals
"""EMPTY = ''' . '''
SHIP = ''' S '''
HIT = ''' X  '''
MISS = ''' # '''
GRID_SIZE = ''' Between 5 to 10 '''
SHIPS = [5, 4, 3, 2, 2]  # Variation sizes of ships
NUM_SHIPS = 5"""


# Function to initialize the game boards
def init_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]


# Function to print the game boards
def print_boards(player, computer, size, hide_comp=True):
    """
    Prints the player and computer game boards side by side.

    :player: The player's game board.
    :computer: The computer's game board.
    :size: The size of the game board.
    :hide_comp: If True, hides the computer's ship positions.
    """
    col_labels = " ".join(chr(65 + i) for i in range(size))
    print(f"{username} Board:      CPU Board:")
    print("   " + col_labels + "   " + "   " + col_labels)
    for i in range(size):
        comp_row = [
            '.' if c == 'S' else c for c in computer[i]
        ] if hide_comp else computer[i]
        row_str = f"{i}  {' '.join(player[i])}   {i}  {' '.join(comp_row)}"
        print(row_str)


# Function to place ships on the board
def place_ship(board, ship_size):
    """
    Randomly places a ship of the given size on the game board.

    :board: The game board to place the ship on.
    :ship_size: The size of the ship.
    """
    while True:
        o = random.choice(['h', 'v'])
        if o == 'h':
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
def conv_input(input_str, size):
    try:
        letter = input_str[0].upper()
        num = int(input_str[1:])
        if 'A' <= letter <= chr(65 + size - 1) and 0 <= num < size:
            x = num
            y = ord(letter) - ord('A')
            return x, y
        else:
            return None, None
    except (ValueError, IndexError):
        return None, None


# Function for the player's turn
def player_turn(comp_board, size):
    while True:
        p_input = input("Enter target (e.g., A0, B1): ")
        x, y = conv_input(p_input, size)
        if (
            x is not None
            and y is not None
            and comp_board[x][y] not in ('X', '#')
        ):
            if comp_board[x][y] == 'S':
                print("Hit!")
                comp_board[x][y] = 'X'
            else:
                print("Miss!")
                comp_board[x][y] = '#'
            break
        else:
            print("Invalid target, try again.")


# Function for the computer's turn
def comp_turn(player_board, size):
    while True:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
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
    return input("Provide your feedback on the game: ")


# Function to play the Battleship game
def play_battleship(size, uname):
    p_board = init_board(size)
    c_board = init_board(size)
    ships = [5, 4, 3, 2, 2]
    for s in ships:
        place_ship(p_board, s)
        place_ship(c_board, s)
    print(f"Welcome {uname} to Battleship war!")
    print_boards(p_board, c_board, size, hide_comp=True)
    print(GAME_INSTRUCTIONS)
    while True:
        player_turn(c_board, size)
        print_boards(p_board, c_board, size, hide_comp=True)
        if is_game_over(c_board):
            print("Congrats, You win! All enemy down.")
            feedback = get_feedback()
            print("Thank you for playing!")
            break
        comp_turn(p_board, size)
        print_boards(p_board, c_board, size, hide_comp=True)
        if is_game_over(p_board):
            print("Game over! The computer sank all your ships. You lose!")
            feedback = get_feedback()
            print("Thank you for playing!")


if __name__ == "__main__":
    while True:
        size = int(input("Enter grid size (5-10): "))
        if 5 <= size <= 10:
            username = input("Enter your Name Captain: ")
            play_battleship(size, username)
            play_again = input("Play another round? (yes/no):").lower()
            if play_again == 'no':
                print("Thank you for playing!")
                break
        else:
            print("Invalid grid size. Enter a value between 5 and 10.")
