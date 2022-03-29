#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(number,rune):
    n = number
    pic = blank_bb
    for x in range(1,n+1):
        frac_rune = scale((n-x+1)*(1/n),rune)
        pic = overlay_frac(1/x,frac_rune,pic)
    return pic

# Test
##show(tree(2, circle_bb))
##show(circle_bb)
##show(overlay_frac(0.2,rcross_bb,sail_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def dual_fractal(rune1,rune2,number):
    n = number
    if n % 2 == 0:
        if n == 2:
            return beside(rune1,stack(rune2,rune2))
        else:
            x = dual_fractal(rune1,rune2,n-2) #rune1
            a = beside(rune2,(stack(x,x)))
            return beside(rune1,stack(a,a))

    if n % 2 == 1:
        if n == 1:
            return rune1
        else:
            y = dual_fractal(rune1,rune2,n-2) #rune2
            b = beside(rune2,(stack(y,y)))
            return beside(rune1,stack(b,b))


def rotating_helix(rune,number):
    n = number
    angle = (2*pi)/n + n
    scaled_rune = scale(2/n,rune)
    pic = blank_bb
    for x in range(2*n):
        radius = 0.5*sin((x)/n)
        temp = translate(radius*cos((x+1)*angle+pi/2),radius*sin((x+1)*angle+pi/2),rotate((x+1)*angle,scaled_rune))
        pic = overlay_frac(1/(x+1),temp,pic)
    return pic


def multi_helix(rune):
    pic = blank_bb
    for x in range(5):
        temp = rotating_helix(rune,7 + x*10)
        pic = overlay_frac(0.25,temp,pic)
##    pic = overlay_frac(0.9,pic,scale(0.7,pentagram_bb))    
    return pic

# Test
show(multi_helix(circle_bb))

##hollusion(overlay(scale(0.8, heart_bb), circle_bb))
