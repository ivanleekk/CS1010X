#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def beside_frac(frac, p1, p2):
    return quarter_turn_left(stack_frac(frac, quarter_turn_right(p1), quarter_turn_right(p2)))

def besiden(n, painter):
	if n==1:
		return painter
	else:
		return beside_frac(1/n, painter, besiden(n-1, painter))

def pi_bb(rune):
    top_layer = besiden(2,rune)
    temp1 = beside_frac(2/3,blank_bb,rune)
    temp2 = beside_frac(1/3,rune,blank_bb)
    second_layer = beside_frac(7/10,beside_frac(3/7, temp1, blank_bb),temp2)
##    temp3 = beside_frac(2/3,rune,blank_bb)
##    temp4 = beside_frac(2/3,blank_bb,rune)
    third_layer = beside_frac(17/100,blank_bb,\
                    beside_frac(13/83,rune, \
                    beside_frac(41/70,blank_bb,\
                    beside_frac(13/29,rune,\
                    beside_frac(5/16,blank_bb,\
                    beside_frac(6/11,rune,blank_bb))))))
    
    fourth_layer = beside_frac(15/100,blank_bb,\
                    beside_frac(14/85,rune, \
                    beside_frac(45/71,blank_bb,\
                    beside_frac(18/26,rune,blank_bb))))
    result = stack_frac(9/10,stack_frac(1/4,top_layer,stackn(8,second_layer)),stack(third_layer,fourth_layer))
    return result

def comp():
    result = pi_bb(black_bb)

    for x in range(2):
        result = pi_bb(result)
    result = beside(result,quarter_turn_right(result))
    result = stack(flip_horiz(flip_vert(result)),result)
    return result
    pass


show(comp())



