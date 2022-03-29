#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def dragonize(order, curve):
    if order == 0:
        return curve
    else:
        prev_level = dragonize(order-1,curve)
        return revert(connect_ends(prev_level,rotate_90(revert(prev_level))))
    pass

# test:

draw_connected_scaled(4096, dragonize(12, unit_line))

