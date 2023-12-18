# Program to find the distance between 2 points

import math

x1 = int(input("Enter values for x1: "))
y1 = int(input("Enter values for y1: "))
x2 = int(input("Enter values for x2: "))
y2 = int(input("Enter values for y2: "))

dist = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print("Distance between the two points:", dist)

