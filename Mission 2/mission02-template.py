#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(rune, number):
    n = number
    pic = rune
    if n == 1:
        return pic
    else:
        return beside(rune, fractal(stack(pic, pic), n-1))


# Test
##show(fractal(make_cross(rcross_bb), 3))
##show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(rune, number):
    og_rune = rune
    for x in range(1, number):
        rune = beside(og_rune, stack(rune, rune))

    return rune

# Test
##show(fractal_iter(make_cross(rcross_bb), 3))
##show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########
def dual_fractal(rune1, rune2, number):
    n = number
    if n % 2 == 0:
        if n == 2:
            return beside(rune1, stack(rune2, rune2))
        else:
            x = dual_fractal(rune1, rune2, n-2)  # rune1
            a = beside(rune2, (stack(x, x)))
            return beside(rune1, stack(a, a))

    if n % 2 == 1:
        if n == 1:
            return rune1
        else:
            y = dual_fractal(rune1, rune2, n-2)  # rune2
            b = beside(rune2, (stack(y, y)))
            return beside(rune1, stack(b, b))

# Test
##show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb),6))
##show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########


def dual_fractal_iter(rune1, rune2, number):
    n = number
    if n % 2 == 1:
        pic = rune1
        for x in range(n-1):
            if x % 2 == 0:
                pic = beside(rune2, stack(pic, pic))
                continue
            elif x % 2 == 1:
                pic = beside(rune1, stack(pic, pic))
                continue
    elif n % 2 == 0:
        pic = rune2
        for x in range(n-1):
            if x % 2 == 0:
                pic = beside(rune1, stack(pic, pic))
                continue
            elif x % 2 == 1:
                pic = beside(rune2, stack(pic, pic))
                continue

    return pic


# Test
##show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 6))
##show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########


def steps(rune1, rune2, rune3, rune4):
    level_1 = beside(blank_bb, stack(rune1, blank_bb))
    level_2 = beside(blank_bb, stack(blank_bb, rune2))
    level_3 = beside(stack(blank_bb, rune3), blank_bb)
    level_4 = beside(stack(rune4, blank_bb), blank_bb)
    pic1 = overlay(overlay(level_4, level_3), overlay(level_2, level_1))
    return pic1


# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
