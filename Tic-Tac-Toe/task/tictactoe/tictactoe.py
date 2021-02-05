board = []
symbols = ['X', 'O', "", "_"]
player = "X"
game_round = 0

game_status = False


def create_board():
    start_position = 0
    end_position = 3

    for i in range(0, 3, 1):
        board.append([])
        for j in range(start_position, end_position, 1):
            board[i].append(' ')

        start_position = end_position
        end_position = end_position + 3


def print_board():
    print("---------")
    for i in range(3):
        for j in range(3):
            if j == 0:
                print('| ' + board[i][j] + ' ', end="")
            else:
                print(board[i][j] + ' ', end="")
        print('|')
    print("---------")


def get_coordinates():
    bool_valid_input = False
    while not bool_valid_input:

        input_coordinates = input("Enter the coordinates: ")
        list_coordinates = input_coordinates.split()

        if list_coordinates[0].isdigit() and list_coordinates[1].isdigit():
            row = int(list_coordinates[0])
            column = int(list_coordinates[1])

            if int(row) > 3 or int(column) > 3:
                print("Coordinates should be from 1 to 3!")
            elif board[int(row) - 1][int(column) - 1] == "X" or board[int(row) - 1][int(column) - 1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                board[int(row) - 1][int(column) - 1] = player

                bool_valid_input = True
        else:
            print("You should enter numbers!")


def not_finished():
    if not three_in_a_row("X") and not three_in_a_row("O"):
        if "" in symbols or "_" in symbols:
            return True


def draw():
    if game_round == 9:
        return True


def three_in_a_row(symbol):
    if board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol:
        return True
    elif board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol:
        return True
    elif board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol:
        return True
    elif board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    elif board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
        return True
    elif board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
        return True
    elif board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
        return True


def impossible():
    if symbols.count("X") - symbols.count("O") > 1 or \
            symbols.count("O") - symbols.count("X") > 1 or \
            three_in_a_row("X") and three_in_a_row("O"):
        return True


def change_player():
    global player

    if player == "O":
        player = "X"
    else:
        player = "O"

    return player


create_board()


while not game_status:
    print_board()
    if impossible():
        print("Impossible")
    elif not_finished() and not draw():
        print("Game not finished")
    elif three_in_a_row("O"):
        print("O wins")
        game_status = True
    elif three_in_a_row("X"):
        print("X wins")
        game_status = True
    elif draw():
        print("Draw")
        game_status = True

    if not game_status:
        get_coordinates()

    game_round = game_round + 1
    change_player()
