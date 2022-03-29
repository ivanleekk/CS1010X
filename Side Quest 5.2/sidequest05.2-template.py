#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line_at_y(0)
    else:
        part_1 = kochize(level-1)
        part_2 = rotate(pi/3)(part_1)
        part_3 = rotate(-pi/3)(part_1)
        part_4 = part_1
        return put_in_standard_position(connect_ends(part_1,connect_ends\
                            (part_2, connect_ends(part_3, part_4))))

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

##show_connected_koch(4, 4000)
##show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    part_1 = kochize(5)
    part_2 = rotate(2*pi/3)(part_1)
    part_3 = rotate(-2*pi/3)(part_1)
    return put_in_standard_position(connect_ends(part_3,connect_ends\
                                                 (part_2,part_1)))
##    return put_in_standard_position()
draw_connected_scaled(10000, snowflake())
