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

""" Convert meters to feet"""
def convert_meters_to_feet(meters):
    # 1 meter = 3.2808 feet
    return meters*3.2808

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

""" Cubic volume in meters^3 """
def volume_cubic(d, w, l):
    return d*w*l
    
""" Sphere volume in meters^3 """
def volume_sphere(r):
    return (4.0/3.0)*pi*r**3
    
""" Circumference of circle """
def circle_circumference(r):
    return (2.0)*pi*r

""" Surface area of circle with radius 2m: """
def surface_circle(r):
    return pi*(r**2)
    
""" Surface area of sphere with radius 2m: """
def surface_sphere(r):
    return 4.0*pi*(r**2)
    
""" Surface area of cube with side 2m: """
def surface_cube(r):
    return 6.0*(r**2)

""" Given a frequency, figure out what it is:"""
def frequency(f):
    if f < 540000:
        return 'Long radio wave'
    elif f < 1600000:
        return 'AM Radio'
    elif f < 88100000:
        return 'Short radio wave'
    elif f < 108100000:
        return 'FM Radio'
    elif f < 300000000:
        return 'WIP'
    elif f < 300000000000:
        return 'Microwaves'
    else:
        return 'WIP'

def test_run():
    """ A ball dropped from a tower. Give height and seconds. """
    drop_from_tower_n1()

    """ A ball dropped from a tower. Given height, find seconds. """
    drop_from_tower_n2()
    
    """ Conversion from ft to meters """
    feet = 10
    print "10 feet in meters: "
    print convert_ft_to_meters(feet)

    """ Conversion from meters to feet """
    meters = 10
    print "10 meters in feet: "
    print convert_meters_to_feet(meters)

    """ Position of a body given acceleration (a), initial velocity (v0), time (t), initial position (p0) """
    # Formula in meters and seconds: p(t) = (1/2)at^2 + v0(t) + p0 
    # In the example below, a=2 m/s^2, v0=2 m/s, t = 2 s, p0 = 0 m 
    print "The position in meters of a body accelerating at 2m/s^2, intial velocity 2m/s, time 2 s, initial position 0 meters: "
    print position_of_accelerating_body(2, 2, 2, 0)

    print "Conversion from polar coordinates (r, theta) to cartesian coordinates (x, y):"
    convert_polar_to_cartesian()
    
    print "Calculate volume (m^3) of a lake 200m deep, 1 km wide, 100 km long: "
    print volume_cubic(200, 1000, 100000)
    
    print "Calculate volume of sphere with radius 2m: "
    print volume_sphere(2)
    
    print "Circumference of a circle with radius 2m: "
    print circle_circumference(2)
    
    print "Surface area of circle with radius 2m: "
    print surface_circle(2)
    
    print "Surface area of sphere with radius 2m: "
    print surface_sphere(2)

    print "Surface area of cube with side 2m: "
    print surface_cube(2)

    print "Given frequency (Hz), this is: "
    print frequency(100)
    
if __name__ == '__main__':
    test_run()
