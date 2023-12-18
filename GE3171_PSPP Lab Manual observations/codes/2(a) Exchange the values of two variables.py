# Program to exchange the value of 2 variables
def swap(a, b):
    print("Before swapping")
    print("Value of a = ", a, " and value of b = ", b)
    a, b = b, a
    print("After swapping")
    print("Value of a = ", a, " and value of b = ", b)


a = int(input("Enter first number"))
b = int(input("Enter second number"))
swap(a, b)
