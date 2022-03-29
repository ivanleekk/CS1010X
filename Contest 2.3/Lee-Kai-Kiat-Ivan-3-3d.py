#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

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
	    
foreground = black_bb
negative = blank_bb

def skyline():
    sky = negative
    water = overlay(negative, foreground)
    building = foreground
    building1= building
    building2= stack_frac(1/6,sky, building)
    building3= stack_frac(1/2,sky, building)
    building4= stack_frac(45/100,sky, building)
    building5= stack_frac(2/3,sky, building)

    close_buildings = beside_frac(1/26, building1, \
                      beside_frac(2/25, negative,\
                      beside_frac(2/23, building2, \
                      beside_frac(2/21, negative, \
                      beside_frac(1/7, building3, \
                      beside_frac(5/12, negative,\
                      beside_frac(1/3, building4, \
                      beside_frac(1/4, negative,building5))))))))

    close_buildings = stack_frac(5/100, sky, close_buildings)

    building6 = stack_frac(1/13,sky, building)
    building7 = stack_frac(1/13,sky, building)
    building8 = stack_frac(1/13,sky, building)
    building9 = stack_frac(22/100,sky, building)
    building10 = building
    building11 = stack_frac(6/10,sky, building)
    building12 = stack_frac(36/100,sky, building)
    building13 = stack_frac(63/100,sky, building)
    building14 = stack_frac(36/100,sky, building)
    building15 = stack_frac(5/7,sky, building)
    building16 = stack_frac(22/100,sky, building)

    middle_buildings =beside_frac(3/100, negative, \
                      beside_frac(5/100, building6, \
                      beside_frac(25/1000, negative,\
                      beside_frac(6/100, building7, \
                      beside_frac(18/100, negative, \
                      beside_frac(12/100, building8, \
                      beside_frac(7/100, negative,\
                      beside_frac(7/100, building9, \
                      beside_frac(13/100, negative,\
                      beside_frac(2/25, building10, \
                      beside_frac(5/100, negative,\
                      beside_frac(7/100, building11, \
                      beside_frac(14/100, building12, \
                      beside_frac(19/100, building13, \
                      beside_frac(22/100, building14, \
                      beside_frac(1/25, negative,\
                      beside_frac(208/1000, building15, \
                      beside_frac(1/2, building16, negative))))))))))))))))))

    middle_buildings = stack_frac(12/100, sky, middle_buildings)


    building17 = stack_frac(3/8,sky, building)
    building18 = stack_frac(7/8,sky, building)
    building19 = stack_frac(1/2,sky, building)
    building20 = stack_frac(1/3,sky, building)
    building21 = stack_frac(1/2,sky,building)
    building22 = stack_frac(28/100,sky, building)
    building23 = stack_frac(3/8,sky, building)
    building24 = stack_frac(1/10,sky, building)
    building25 = stack_frac(1/8,sky, building)
    building26 = building
    building27 = stack_frac(1/16,sky, building)

    far_buildings =   beside_frac(1/13, negative, \
                      beside_frac(1/12, building17, \
                      beside_frac(54/1000, negative,\
                      beside_frac(4/100, building18, \
                      beside_frac(2/100, negative, \
                      beside_frac(27/1000, building19, \
                      beside_frac(66/1000, building20, \
                      beside_frac(6/100, negative,\
                      beside_frac(6/100, building21, \
                      beside_frac(7/100, building22, \
                      beside_frac(1/10, negative,\
                      beside_frac(4/25, building23, \
                      beside_frac(9/100, building24, \
                      beside_frac(13/100, negative,\
                      beside_frac(19/100, building25, \
                      beside_frac(37/1000, negative,\
                      beside_frac(15/100, building26, \
                      beside_frac(1/4, negative,\
                      beside_frac(3/10, building27, negative)))))))))))))))))))

                                  
    all_buildings = overlay(close_buildings,overlay(middle_buildings,overlay(far_buildings,sky)))
    with_sky = stack_frac(47/100, sky, all_buildings)
    water_with_reflect = overlay(sky, overlay_frac(1/10, flip_vert(all_buildings),water))
    result = stack_frac(66/100, with_sky, water_with_reflect)
    return result
    pass

##show(skyline())

# Use one of the following methods to display your rune:
stereogram(skyline())
##anaglyph(skyline())
##hollusion(skyline())
