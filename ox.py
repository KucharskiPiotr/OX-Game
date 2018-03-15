"""
    Simple console OX game
    Author: Piotr Kucharski
"""

# Global variable to set draw
draw = False

def print_field(table):
    print(" %c | %c | %c \n" % (table[6], table[7], table[8]) + 
          "-----------\n" +
          " %c | %c | %c \n" % (table[3], table[4], table[5]) +
          "-----------\n" +
          " %c | %c | %c \n" % (table[0], table[1], table[2]))

def get_input():
    """
    Method gets index of field to be set by user sign
    returns: index of field as table index
    """

    print(" 7 | 8 | 9 \n" +
          " 4 | 5 | 6 \n" +
          " 1 | 2 | 3 \n Podaj miejsce: ")
    a = int(input()) - 1
    
    if a < 0 or a > 8:
        print("Wrong field index!")
        get_input()

    return a

def does_game_last(table):
    """
    Method checks if game has finished
    returns: False when game is finished, True otherwise
    """
    global draw

    # Vertical win
    for i in range(0, 9, 4):
        if table[i] == table[(i + 3) % 9] == table[(i + 6) % 9] != ' ':
            return False

    # Horizontal win
    for i in range(1, 8, 3):
        table[i - 1] == table[i] == table[i + 1] != ' ':
            return False

    # Cross win    
    if table[4] == table[6] == table[2] != ' ' or table[4] == table[0] == table[8] != ' ':
        return False


    # Check if move is still possible or it's draw
    for i in range(0, 8):
        if(table[i] == ' '):
            return True
    else:
        draw = True
        return False

    return True

def main():
    """
    Main game loop
    """

    is_game = True
    x_turn = True
    table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while(is_game):
        print_field(table)
        print("\n")
        if x_turn:
            table[get_input()] = 'X'
            x_turn = False
        else:
            table[get_input()] = 'O'
            x_turn = True
        is_game = does_game_last(table)
    
    print("\n")
    print_field(table)

    # Decide who won the game
    if draw:
        print("Draw!\n")
    else:
        if x_turn:
            print('O player wins!\n')
        else:
            print('X player wins!\n')
        
main()