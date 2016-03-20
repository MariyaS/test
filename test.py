""" For practice of basic physics problems. """

from math import log, sqrt

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

def test_run():
    """ A ball dropped from a tower. Give height and seconds. """
    drop_from_tower_n1()

    """ A ball dropped from a tower. Given height, find seconds. """
    drop_from_tower_n2()

if __name__ == '__main__':
    test_run()