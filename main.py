import numpy as np

board = []
dimension = 0
game_on = True
winner = None
current_player = "X"
x_score = 0
o_score = 0
score_dic = {1: 0, 2: 0, 3: 2, 4: 10, 5: 50, 6: 100, 7: 200, 8: 300, 9: 400, 10: 5000}


def display_board():
    for line in board:
        print(' | '.join(map(str, line)))


def display_scores():
    print("X score: " + str(x_score) + " O score: " + str(o_score))


def play_game():
    initialize_board()
    display_board()
    while game_on:
        handle_turn(current_player)
        check_if_game_over()
        display_scores()
        flip_player()
    if winner is None:
        print("No one won.")
    else:
        print(winner + " won.")


def initialize_board():
    global board
    global dimension
    dimension = input("Choose the N value of the NxN board: ")
    while not dimension.isdigit():
        dimension = input("Invalid input. Choose a natural number: ")
    dimension = int(dimension)
    board = [["-" for _ in range(dimension)] for _ in range(dimension)]


def handle_turn(player):
    keep_handling = True
    while keep_handling:
        row = input("Choose a row: ")
        while not (row.isdigit() and int(row) <= dimension):
            row = input("Incorrect value for row. Choose a natural number equal or less than dimension: ")
        row = int(row) - 1
        column = input("Choose a column: ")
        while not (column.isdigit() and int(column) <= dimension):
            column = input("Incorrect value for column. Choose a natural number equal or less than dimension: ")
        column = int(column) - 1
        if board[row][column] == "-":
            board[row][column] = player
            keep_handling = False
        else:
            print("Position on the board already claimed! Choose another position.")
    display_board()


def check_if_game_over():
    global x_score
    global o_score
    if current_player == "X":
        x_score = 0
    else:
        o_score = 0
    check_points()
    check_end()


def check_points():
    global x_score
    global o_score
    lengths = []
    lengths.extend(check_rows())
    lengths.extend(check_columns())
    lengths.extend(check_diagonals())
    for c in lengths:
        if current_player == "X":
            x_score += score_dic[c]
        else:
            o_score += score_dic[c]


def get_lengths(player, row):
    num_string = np.array([1 if _ == player else 0 for _ in row])
    counter = []
    c = 1
    for j, element in enumerate(np.diff(num_string)):
        if element == 0:
            c += 1
        elif element == -1:
            counter.append(c)
            c = 1
        else:
            c = 1
    if num_string[-1] == 1:
        counter.append(c)
    return counter


def check_rows():
    length_counter = []
    for i in range(dimension):
        if current_player in board[i]:
            length_counter.extend(get_lengths(current_player, board[i]))
    return length_counter


def check_columns():
    length_counter = []
    for i in range(0, dimension):
        k = []
        # generate column
        for j in range(0, dimension):
            k.append(board[j][i])
        if current_player in k:
            length_counter.extend(get_lengths(current_player, k))
    return length_counter


def check_diagonals():
    d = get_diagonals()
    length_counter = []
    for diagonal in d:
        if current_player in diagonal:
            length_counter.extend(get_lengths(current_player, diagonal))
    return length_counter


def get_diagonals():
    n = dimension
    d = [[board[y - x][x] for x in range(dimension) if 0 <= y - x < dimension] for y in range(2 * dimension - 1)]
    d2 = [[row[i+offset] for i, row in enumerate(board) if 0 <= i + offset < len(row)] for offset in range(-n + 1, n)]
    d.extend(d2)
    d = [x for x in d if len(x) > 2]
    return d


def check_end():
    global game_on
    global winner
    game_over = True
    for i in range(dimension):
        game_over = game_over and "-" not in board[i]
    game_over = game_over or x_score >= 50 or o_score >= 50
    if x_score >= 50:
        winner = "X"
    elif o_score >= 50:
        winner = "O"
    game_on = not game_over
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


play_game()
