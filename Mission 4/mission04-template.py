#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *


def unit_line_at_y ( y ):
    return lambda t : make_point (t , y )
a_line = unit_line_at_y ( 0 )
draw_connected(200, a_line)

##########
# Task 1 #
##########

# (a)
# unit_line_at_y: (Number) -> Curve

# (b)
# a_line: (Empty) -> Curve

# (c)
def vertical_line(point, length):
    o_x = x_of(point)
    o_y = y_of(point)
    def output_line(t):
        return make_point(o_x,o_y + t*length)
    return output_line

##draw_connected(200, vertical_line(make_point(0.1, 0.1), 0.4))

# (d)
# vertical_line: (Point,Number) -> Curve

## (e)
##draw_connected(200, vertical_line(make_point(0.5,0.25),0.5))

##########
# Task 2 #
##########

# (a)
# By using this function once, using a scaled viewport, points that were on the left should now appear on the right and vice versa, but still at the same y-value. Furthermore using this function twice should yield the same curve as the original with no changes. If both conditions are met, then this fucntion works properly.


# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt),y_of(pt))

    return reflected_curve
	
##draw_connected_scaled(200, arc)
##draw_connected_scaled(200, reflect_through_y_axis(arc))
##draw_connected_scaled(200, reflect_through_y_axis(reflect_through_y_axis(arc)))
