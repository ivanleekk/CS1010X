#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########


def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


def flatten(mat):
    return [num for row in mat for num in row]


###########
# Task 1  #
###########


def new_game_matrix(n):
    row = [0] * n
    return [row[:] for i in range(n)]


def has_zero(mat):
    flat = flatten(mat)
    return 0 in flat


def add_two(mat):
    if has_zero(mat):
        row_length = len(mat[0])
        flat = flatten(mat)
        zero_loc = []
        for x in range(len(flat)):
            if flat[x] == 0:
                zero_loc.append([x // row_length, x % row_length])
        random_loc = zero_loc[randint(0, len(zero_loc) - 1)]
        mat[random_loc[0]][random_loc[1]] = 2
        return mat
    else:
        return mat


game = new_game_matrix(4)
print(game)
game = add_two(game)
print(game)


###########
# Task 2  #
###########


def game_status(mat):
    flat = flatten(mat)
    if 2048 in flat:
        return "win"
    elif has_zero(mat):
        return "not over"
    else:
        row_length = len(mat[0])
        for x in range(row_length):
            for y in range(row_length):
                a, b = x + 1, y + 1
                if a < row_length:  # check down
                    if mat[x][y] == mat[a][y]:
                        return "not over"
                if b < row_length:  # check right
                    if mat[x][y] == mat[x][b]:
                        return "not over"
        return "lose"


game = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(game_status(game))

###########
# Task 3a #
###########


def transpose(mat):
    result = []
    for x in range(len(mat[0])):
        temp = []
        for y in range(len(mat)):
            temp.append(mat[y][x])
        result.append(temp)
    return result


print(transpose(game))
print(transpose([[1, 2, 3], [4, 5, 6]]))


###########
# Task 3b #
###########


def reverse(mat):
    result = []
    for x in range(len(mat)):
        result.append([mat[x][i] for i in range(len(mat[x]) - 1, -1, -1)])
    return result


print(reverse(game))


############
# Task 3ci #
############


def merge_left(mat):
    result = []
    row_length = len(mat[0])
    # breakpoint()
    increment = 0
    for row in mat:
        indexes = [x for x in range(len(row)) if row[x] != 0]
        if len(indexes) == 0:
            result.append([0 for x in range(row_length)])
            continue
        temp = []
        current_tile = indexes.pop(0)
        while len(indexes) >= 0:
            if len(indexes) != 0:
                next_tile = indexes.pop(0)
            else:
                temp.append(row[current_tile])
                break
            if row[current_tile] == row[next_tile]:
                up = row[current_tile] + row[next_tile]
                increment += up
                temp.append(up)
                if len(indexes) == 0:
                    break
                current_tile = indexes.pop(0)
            else:
                temp.append(row[current_tile])
                current_tile = next_tile
        temp.extend([0 for x in range(row_length - len(temp))])
        result.append(temp)
    return (result, result != mat, increment)


test = [
    [2, 2, 0, 4],
    [4, 4, 2, 0],
    [2, 2, 2, 2],
    [0, 0, 0, 4],
    [16, 0, 8, 16],
    [0, 0, 0, 0],
]
print(merge_left(test))


#############
# Task 3cii #
#############


def merge_right(mat):
    temp = reverse(mat)
    temp = merge_left(temp)
    result = (reverse(temp[0]), temp[1], temp[2])
    return result


def merge_up(mat):
    temp = transpose(mat)
    temp = merge_left(temp)
    result = (transpose(temp[0]), temp[1], temp[2])
    return result


def merge_down(mat):
    temp = transpose(mat)
    temp = reverse(temp)
    temp = merge_left(temp)
    temp = (reverse(temp[0]), temp[1], temp[2])
    result = (transpose(temp[0]), temp[1], temp[2])
    return result


game = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
print(merge_right(game))
print(merge_up(game))
print(merge_down(game))

###########
# Task 3d #
###########


def text_play():
    def print_game(mat, score):
        for row in mat:
            print("".join(map(lambda x: str(x).rjust(5), row)))
        print("score: " + str(score))

    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input("Enter W, A, S, D or Q: ")
        move = move.lower()
        if move not in ("w", "a", "s", "d", "q"):
            print("Invalid input!")
            continue
        if move == "q":
            print("Quitting game.")
            return
        move_funct = {
            "w": merge_up,
            "a": merge_left,
            "s": merge_down,
            "d": merge_right,
        }[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print("Move invalid!")
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return


# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
# text_play()


# How would you test that the winning condition works?
# Your answer: I would create my own matrix with 2048 inside and test the function game_status() to see if it will trigger
#


##########
# Task 4 #
##########
def post_add(state):
    if state[1] == True:
        state[0] = add_two(state[0])
        return (state, state[1])
    else:
        return state


def make_state(matrix, total_score):
    pass


def get_matrix(state):
    return state[0]


def get_score(state):
    return state[2]


def make_new_game(n):
    mat = add_two(add_two(new_game_matrix(n)))
    return mat


def left(state):
    result = merge_left(state[0])
    result = post_add(result)
    return (result, result[1])


def right(state):
    result = merge_right(state[0])
    result = post_add(result)
    return (result, result[1])


def up(state):
    result = merge_up(state[0])
    result = post_add(result)
    return (result, result[1])


def down(state):
    result = merge_down(state[0])
    result = post_add(result)
    return (result, result[1])


# Do not edit this #
game_logic = {
    "make_new_game": make_new_game,
    "game_status": game_status,
    "get_score": get_score,
    "get_matrix": get_matrix,
    "up": up,
    "down": down,
    "left": left,
    "right": right,
    "undo": lambda state: (state, False),
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
gamegrid = GameGrid(game_logic)


#################
# Optional Task #
#################

###########
# Task 5i #
###########


def make_new_record(mat, increment):
    "Your answer here"


def get_record_matrix(record):
    "Your answer here"


def get_record_increment(record):
    "Your answer here"


############
# Task 5ii #
############


def make_new_records():
    "Your answer here"


def push_record(new_record, stack_of_records):
    "Your answer here"


def is_empty(stack_of_records):
    "Your answer here"


def pop_record(stack_of_records):
    "Your answer here"


#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"


def get_matrix(state):
    "Your answer here"


def get_score(state):
    return state[2]


def make_new_game(n):
    mat = add_two(add_two(new_game_matrix(n)))
    return mat


def left(state):
    "Your answer here"


def right(state):
    "Your answer here"


def up(state):
    "Your answer here"


def down(state):
    "Your answer here"


# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"


def undo(state):
    "Your answer here"


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': undo
##}
# gamegrid = GameGrid(game_logic)
