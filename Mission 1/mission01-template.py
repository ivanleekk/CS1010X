#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(top_right, bot_right, bot_left, top_left):
    # Fill in code here
    return beside(stack(top_left, bot_left),stack(top_right, bot_right))


# Test
##show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(rune):
    # Fill in code here
    return beside(rune, stack(rune, rune))

# Test
show(simple_fractal(make_cross(rcross_bb)))
