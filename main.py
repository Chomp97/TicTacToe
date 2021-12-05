board = []
dimension = 0
game_on = True
winner = None
current_player = "X"
x_score = 0
o_score = 0


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
    valid = False
    while not valid:
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
            valid = True
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
    check_rows()
    check_columns()
    check_diagonals()


def add_points_to_player(points):
    global x_score
    global o_score
    if current_player == "X":
        x_score += points
    else:
        o_score += points


def check_rows():
    for i in range(0, dimension):
        for j in range(0, dimension):
            if j + 4 < dimension:
                if current_player in set(board[i][j:j + 5]) and len(set(board[i][j:j + 5])) == 1:
                    add_points_to_player(50)
                    j += 5
                elif current_player in set(board[i][j:j + 4]) and len(set(board[i][j:j + 4])) == 1:
                    add_points_to_player(10)
                    j += 4
                elif current_player in set(board[i][j:j + 3]) and len(set(board[i][j:j + 3])) == 1:
                    add_points_to_player(2)
                    j += 3
            elif j + 3 < dimension:
                if current_player in set(board[i][j:j + 4]) and len(set(board[i][j:j + 4])) == 1:
                    add_points_to_player(10)
                    j += 4
                elif current_player in set(board[i][j:j + 3]) and len(set(board[i][j:j + 3])) == 1:
                    add_points_to_player(2)
                    j += 3
            elif j + 2 < dimension:
                if current_player in set(board[i][j:j + 3]) and len(set(board[i][j:j + 3])) == 1:
                    add_points_to_player(2)
                    j += 3
    return


def check_columns():
    for i in range(0, dimension):
        k = []
        for j in range(0, dimension):
            k.append(board[j][i])
        for n in range(0, dimension):
            if n + 4 < dimension:
                if current_player in set(k[n:n + 5]) and len(set(k[n:n + 5])) == 1:
                    add_points_to_player(50)
                    n += 5
                elif current_player in set(k[n:n + 4]) and len(set(k[n:n + 4])) == 1:
                    add_points_to_player(10)
                    n += 4
                elif current_player in set(k[n:n + 3]) and len(set(k[n:n + 3])) == 1:
                    add_points_to_player(2)
                    n += 3
            elif n + 3 < dimension:
                if current_player in set(k[n:n + 4]) and len(set(k[n:n + 4])) == 1:
                    add_points_to_player(10)
                    n += 4
                elif current_player in set(k[n:n + 3]) and len(set(k[n:n + 3])) == 1:
                    add_points_to_player(2)
                    n += 3
            elif n + 2 < dimension:
                if current_player in set(k[n:n + 3]) and len(set(k[n:n + 3])) == 1:
                    add_points_to_player(2)
                    n += 3


def check_diagonals():
    d = get_diagonals()
    for diagonal in d:
        leng = len(diagonal)
        for n in range(0, leng):
            if n + 4 < leng:
                if current_player in set(diagonal[n:n+5]) and len(set(diagonal[n:n+5])) == 1:
                    add_points_to_player(50)
                    n += 5
                elif current_player in set(diagonal[n:n+4]) and len(set(diagonal[n:n+4])) == 1:
                    add_points_to_player(10)
                    n += 4
                elif current_player in set(diagonal[n:n+3]) and len(set(diagonal[n:n+3])) == 1:
                    add_points_to_player(2)
                    n += 3
            elif n + 3 < leng:
                if current_player in set(diagonal[n:n + 4]) and len(set(diagonal[n:n + 4])) == 1:
                    add_points_to_player(10)
                    n += 4
                elif current_player in set(diagonal[n:n + 3]) and len(set(diagonal[n:n + 3])) == 1:
                    add_points_to_player(2)
                    n += 3
            elif n + 2 < leng:
                if current_player in set(diagonal[n:n + 3]) and len(set(diagonal[n:n + 3])) == 1:
                    add_points_to_player(2)
                    n += 3


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
