draw = False

def print_field(tablica):
    print(" %c | %c | %c \n" % (tablica[6], tablica[7], tablica[8]) + 
          "-----------\n" +
          " %c | %c | %c \n" % (tablica[3], tablica[4], tablica[5]) +
          "-----------\n" +
          " %c | %c | %c \n" % (tablica[0], tablica[1], tablica[2]))

def get_input():
    print(" 7 | 8 | 9 \n" +
          " 4 | 5 | 6 \n" +
          " 1 | 2 | 3 \n Podaj miejsce: ")
    a = int(input()) - 1
    
    if a < 0 or a > 8:
        print("Wrong field index!")
        get_input()

    return a

def is_game_finished(tablica):
    global draw

    if((tablica[6] == tablica[7] == tablica[8] and tablica[6] != ' ' and tablica[7] != ' ' and tablica[8] != ' ') or 
        (tablica[5] == tablica[4] == tablica[3] and tablica[5] != ' ' and tablica[4] != ' ' and tablica[3] != ' ') or
        (tablica[2] == tablica[1] == tablica[0] and tablica[2] != ' ' and tablica[1] != ' ' and tablica[0] != ' ') or
        (tablica[6] == tablica[4] == tablica[2] and tablica[6] != ' ' and tablica[4] != ' ' and tablica[2] != ' ') or
        (tablica[8] == tablica[4] == tablica[0] and tablica[8] != ' ' and tablica[4] != ' ' and tablica[0] != ' ') or
        (tablica[6] == tablica[3] == tablica[0] and tablica[6] != ' ' and tablica[3] != ' ' and tablica[0] != ' ') or
        (tablica[7] == tablica[4] == tablica[1] and tablica[7] != ' ' and tablica[4] != ' ' and tablica[1] != ' ') or
        (tablica[8] == tablica[5] == tablica[2] and tablica[8] != ' ' and tablica[5] != ' ' and tablica[2] != ' ')):
        return False
    
    for i in range(0, 8):
        if(tablica[i] == ' '):
            return True
    else:
        draw = True
        return False

    return True

def main():
    is_game = True
    x_turn = True
    tablica = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while(is_game):
        print_field(tablica)
        print("\n")
        if x_turn:
            tablica[get_input()] = 'X'
            x_turn = False
        else:
            tablica[get_input()] = 'O'
            x_turn = True
        is_game = is_game_finished(tablica)
    
    print("\n")
    print_field(tablica)
    if draw:
        print("Draw!\n")
    else:
        if x_turn:
            print('O player wins!\n')
        else:
            print('X player wins!\n')
        
main()