def is_leap_year(year):
    # DONE: do not need to modify
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False


def is_valid(d, m, y):
    # DONE: do not need to modify
    # d, m, y represents day, month, and year in integer.
    if y < 1970 or y > 9999:
        return False
    if m <= 0 or m > 12:
        return False
    if d <= 0 or d > 31:
        return False

    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False

    if is_leap_year(y):
        if m == 2 and d > 29:
            return False
    else:
        if m == 2 and d > 28:
            return False

    return True


def get_day_month_year(date):
    # TODO: split the date and return a tuple of integer (day, month, year)
    d, m, y = map(int, date.split("/"))
    return (d, m, y)


def less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):
    if (
        start_year > end_year
        or start_year == end_year
        and start_mon > end_mon
        or start_year == end_year
        and start_mon == end_mon
        and start_day > end_day
    ):
        return False
    else:
        return True


def next_date(d, m, y):
    # TODO: get the next date from the current date (d, m, y)
    # return a tuple of integer (day, month, year).
    if is_valid(d + 1, m, y):
        return (d + 1, m, y)
    elif is_valid(1, m + 1, y):
        return (1, m + 1, y)
    else:
        return (1, 1, y + 1)


def count_days(start_date, end_date):
    # date is represented as a string in format dd/mm/yyyy
    start_day, start_mon, start_year = get_day_month_year(start_date)
    end_day, end_mon, end_year = get_day_month_year(end_date)

    # TODO: check for data validity here #
    # if start date is not valid...
    # if end date is not valid...
    # if start date > end date...

    if not is_valid(start_day, start_mon, start_year):
        raise Exception("Not a valid date: " + start_date)
    elif not is_valid(end_day, end_mon, end_year):
        raise Exception("Not a valid date: " + end_date)
    elif not less_than_equal(
        start_day, start_mon, start_year, end_day, end_mon, end_year
    ):
        raise Exception("Start date must be less than or equal end date.")

        # lazy - let the computer count from start date to end date
    count = 0
    while less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):
        count = count + 1
        start_day, start_mon, start_year = next_date(start_day, start_mon, start_year)

    # exclude end date
    return count - 1


def faster_pascal(row, col):
    # your code here
    storage = [[0 for x in range(y + 2)] for y in range(row + 2)]

    def pascal(irow, icol):
        if icol == 1 or icol == irow:
            storage[irow][icol] = 1
            return 1
        else:
            if storage[irow][icol] != 0:
                return storage[irow][icol]
            else:
                storage[irow][icol] = pascal(irow - 1, icol) + pascal(
                    irow - 1, icol - 1
                )
            return storage[irow][icol]

    return pascal(row, col)
    pass


# print(faster_pascal(100, 45))
# print(faster_pascal(500, 3))

# table = {}  # table to memoize computed values


# def num_of_paths(n, m):
# if (n, m) in table.keys():
#     return table[n, m]
# elif n == 1 and m >= 1 or m == 1 and n >= 1:
#     table[n, m] = 1
#     return table[n, m]
# else:
#     table[n, m] = num_of_paths(n - 1, m) + num_of_paths(n, m - 1)
#     return table[n, m]
#     pass


def num_of_paths(maze):
    maze_table = {}
    rows = len(maze)
    cols = len(maze[0])
    for row in range(rows):
        if maze[row][0] == 1:
            maze_table[row, 0] = 1
        else:
            for ro in range(row, rows):
                maze_table[0, ro] = 0
            break
    for col in range(cols):
        if maze[0][col] == 1:
            maze_table[0, col] = 1
        else:
            for co in range(col, cols):
                maze_table[co, 0] = 0
            break
    print(maze_table)

    def dp(n, m):
        if (n, m) in maze_table.keys():
            return maze_table[n, m]

        elif n < 0 or m < 0:
            return 0

        elif maze[n][m] == 0:
            maze_table[n, m] = 0
            return 0

        else:
            maze_table[n, m] = dp(n - 1, m) + dp(n, m - 1)
            return maze_table[n, m]

    return dp(rows - 1, cols - 1)
    pass


# Do NOT modify
maze1 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
    (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
    (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
    (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
    (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
    (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
    (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
    (1, 1, 0, 1, 0, 1, 0, 1, 1, 1),
)


maze2 = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1),
)

maze3 = (
    (1, 0, 1, 1),
    (1, 0, 1, 1),
    (1, 0, 1, 1),
    (1, 0, 1, 1),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
)

print(num_of_paths(maze1))
print(num_of_paths(maze2))
print(num_of_paths(maze3))
