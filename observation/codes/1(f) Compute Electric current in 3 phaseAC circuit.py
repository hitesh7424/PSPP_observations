import math

# Program to compute electric current in a 3-phase AC circuit

v = int(input("Enter the voltage of the AC Circuit: "))
c = int(input("Enter the current value of the AC Circuit: "))
pf = float(input("Enter the power factor of the AC Circuit: "))

ec = math.sqrt(3) * v * c * pf
print("Electric current in 3-phase AC circuit:", ec)

