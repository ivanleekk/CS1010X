#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    def connected_curve(t):
        if t<0.5:
            return curve1(2*t)
        else:
            return transform_curve2(curve2)(2*t-1)
    end_curve1 = curve1(1)
    start_curve2 = curve2(0)
    endx = x_of(end_curve1)
    endy = y_of(end_curve1)
    startx = x_of(start_curve2)
    starty = y_of(start_curve2)
    transform_curve2 = translate(endx-startx,endy-starty)
    return connected_curve
    
    pass

##draw_connected_scaled(200, connect_ends(arc, unit_line))
##draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))

##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    "your solution here!"
    def gosper_any_curve(level,curve):
        return repeated(gosperize,level)(curve)
    gospered_curve = gosper_any_curve(level,initial_curve)
    
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(gospered_curve)
    draw_points(num_points,squeezed_curve)
    pass
##show_points_gosper(5, 500, arc)
##########
# Task 3 #
##########

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

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
