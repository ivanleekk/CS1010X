#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    x_v = velocity * cos(radians(angle))
    y_v = velocity * sin(radians(angle))
    return (x_v,y_v)
    pass

##print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    def acceleration_per_planet(planet,current_x, current_y):
        x_p = get_x_coordinate(planet)
        y_p = get_y_coordinate(planet)
        delta_x = current_x - x_p
        delta_y = current_y - y_p
        mass = get_mass(planet)
        distance = sqrt((delta_x**2 + delta_y**2))
        def acceleration(mass, distance, d_x):
            return((G * mass * d_x)/distance**3)
        return (acceleration(mass,distance,delta_x),acceleration(mass,distance,delta_y))

    t_x = ()
    for planet in planets:
        t_x += (acceleration_per_planet(planet,current_x,current_y),)

    final = (0,0)
    for a in t_x:
        final = (final[0] - a[0], final[1] - a[1])
    return final
    pass #remove and replace with your code

##print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    x, y, v_x, v_y = Y
    vx = v_x
    vy = v_y
    a = calculate_total_acceleration(planets, x, y)
    ax = a[0]
    ay = a[1]
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
##print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(63, 27)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
