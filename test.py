""" For practice of basic physics problems. """

from math import log, sqrt
# for conversion from polar to cartesian coordinates
from math import sin, cos, pi

""" Example 1. """
def drop_from_tower_n1():
    h = float(input("Enter height of tower (meters): "))
    t = float(input("Enter the time interval (seconds): "))
    v_initial = 0
    """ Gravity, g=9.81 ms^(-2) """
    g = 9.81
    air_resistance = 0
    """ s = (1/2) gt^2"""
    s = g *t**2 / 2
    print"The height of the ball is: ", h-s, " meters."

""" Example 2. """
def drop_from_tower_n2():
    h = float(input("Enter height of tower (meters): "))
    v_initial = 0
    """ Gravity, g=9.81 ms^(-2) """
    g = 9.81
    air_resistance = 0
    """ Formula t = sqrt(2s/g)"""
    t = sqrt(2*h/g)
    print"The time the ball takes to hit the ground: ", t, " seconds."

""" Convert feet to meters """
def convert_ft_to_meters(feet):
    # 1 foot = 12 inches
    # 1 inch = 2.54 cm = 0.0254m
    return feet*12*0.0254

""" Position of accelerating body. """
def position_of_accelerating_body(a, v0, t, p0):
    return (0.5)*a*(t**2) + v0*t + p0

""" Convert polar coordinates to cartesian coordinates """
def convert_polar_to_cartesian():
    r = float(input("Enter r: "))
    degrees = float(input("Enter theta in degrees: "))
    
    # Angle in radians
    theta = degrees * pi / 180
    
    # Cartesian coordinates equivalent to the polar coordinates
    x = r * cos(theta)
    y = r * sin(theta)
    
    print(" x = ", x, " y = ", y)

def test_run():
    """ A ball dropped from a tower. Give height and seconds. """
    drop_from_tower_n1()

    """ A ball dropped from a tower. Given height, find seconds. """
    drop_from_tower_n2()
    
    """ Conversion from ft to meters """
    feet = 10
    print "10 feet in meters: "
    print convert_ft_to_meters(feet)

    """ Position of a body given acceleration (a), initial velocity (v0), time (t), initial position (p0) """
    # Formula in meters and seconds: p(t) = (1/2)at^2 + v0(t) + p0 
    # In the example below, a=2 m/s^2, v0=2 m/s, t = 2 s, p0 = 0 m 
    print "The position in meters of a body accelerating at 2m/s^2, intial velocity 2m/s, time 2 s, initial position 0 meters: "
    print position_of_accelerating_body(2, 2, 2, 0)

    print "Conversion from polar coordinates (r, theta) to cartesian coordinates (x, y):"
    convert_polar_to_cartesian()
    
if __name__ == '__main__':
    test_run()
