# 1(f) Program to calculate the weight of a steel bar

d = int(input("Enter diameter of the steel bar "))
l = int(input("Enter length of the steel bar "))
wt = (pow(d, 2) / 162.2) * l
print("Weight of the steel bar with diameter ", d, " and length ", l, " is ", wt)
