#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program calculates the circumference and area of a circle

import math


def main():
    # assigns user input as a value for variable radius
    radius = float(input("What is the radius of your circle: "))
    print("")

    # calculates  and prints circumference and area of a circle using variable radius and operation math.pi
    print("The circumference of the circle is: {:.2f}".format(radius * (math.pi * 2)))

    print("The area of the circle is: {:.2f}".format(math.pi * (radius**2)))


if __name__ == "__main__":
    main() # runs the program 
