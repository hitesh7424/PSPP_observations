# Program to print area of a circle using function

import math


def circle(r):
    return math.pi * r * r, 2 * math.pi * r


rad = int(input("Enter the radius of the circle: "))
area, circum = circle(rad)

print("Radius of circle:", rad)
print("Area of circle: ", round(area, 2))
