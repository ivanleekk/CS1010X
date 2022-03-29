#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########
def fractal(rune,number):
    n = number
    pic = rune
    if n == 1:
        return pic
    else:
        return stack(rune,fractal(beside(pic,pic),n-1))


# Test
##show(fractal(make_cross(rcross_bb), 7))




def fractal_iter(rune,number):
    n = number
    pic = rune
    for x in range(0,n-1):
        pic = stack(rune,beside(pic,pic))
    return pic

# Test
##show(fractal_iter(make_cross(rcross_bb), 7))


def dual_fractal(rune1, rune2, number):
    n = number
    pic = rune2
    if n == 1:
        return rune1
    elif n == 2:
        return stack(rune1,beside(rune2,rune2))
    elif n % 2 == 0:
        return dual_fractal(dual_fractal(rune1, rune2, 1),dual_fractal(rune1, rune2, 2),n-1)
    elif n % 2 == 1:
        return dual_fractal(dual_fractal(rune1, rune2, 2),dual_fractal(rune1, rune2, 1), n-1)
    ##    if n == 0:
##        return
##    elif n % 2 == 0:
##        return stack(rune1,beside(dual_fractal(rune1, rune2, n-1), dual_fractal(rune1, rune2, n-1)))
##    elif n % 2 == 1:
##        return stack(rune2,beside(dual_fractal(rune1, rune2, n-1), dual_fractal(rune1, rune2, n-1)))
    
        
    pass

##Test
show(dual_fractal(make_cross(rcross_bb),make_cross(nova_bb),3))
