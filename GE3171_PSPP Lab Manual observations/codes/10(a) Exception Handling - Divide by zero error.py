# Program to handle exception Divide by zero
try:
    n1 = int(input("Enter first number"))
    n2 = int(input("Enter second number"))
    x = n1 / n2
    print(n1, " / ", n2, " =", x)
    y = 22 / 0
    print(y)
except ZeroDivisionError:
    print("Tried to divide by zero")
