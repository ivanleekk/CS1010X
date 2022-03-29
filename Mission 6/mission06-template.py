#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        left_curve = rotate ( theta )( curve_fn )
        right_curve = rotate ( - theta )( curve_fn )
        return put_in_standard_position(connect_ends(left_curve,right_curve))
    return inner_gosperize


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda: gosper_curve(100),1000))

# Time measurements
##298.9991
##301.5009
##298.91290000000004
##302.2526
##301.363
##average time
##300.6057

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda : gosper_curve_with_angle(100, lambda lvl : pi/4), 1 ))

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>
##314.41510000000005
##315.38469999999995
##316.27559999999994
##308.12170000000003
##314.5069
##average time
##313.7408
#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda : your_gosper_curve_with_angle(100, lambda lvl : pi/4), 1 ))

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>
##95466.045
##94800.6455
##96774.0984
##99971.0601
##95470.8048
##average time
##96496.5308

# Conclusion:
#  As can be seen from the results above, functions which are more customised(have more values pre-defined) such as gosper_curve generally run faster than functions which are more customisable(can pass in other functions to alter it) such as gosper_curve_with_angle


##########
# Task 2 #
##########

#  1) your explanation here
##Yes it still works and achieves the same purpose because you are still computing using the same values

#  2) your explanation here
##In rotate(), by using 'pt', you are saving the value of curve at that point into the variable 'pt' which thus lets you find the x and y value of that point quickly by reading the varaible.
##In joe_rotate() however, to find the value of x and y, the program computes the value of the curve at that point once each, for both x and y.
##As gosper_curve() is made using repeated(), it creates a recursive function.
##When used in gosper_curve(), the time taken for joe_rotate() compared to rotate() is doubled per level and thus becomes exponential as it has a time complexity of 2**n.


##########
# Task 3 #
##########


#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>         <4>
#                      2         <5>         <10>
#                      3         <7>         <22>
#                      4         <9>         <46>
#                      5         <11>         <94>
#
#  Evidence of exponential growth in joe_rotate.
