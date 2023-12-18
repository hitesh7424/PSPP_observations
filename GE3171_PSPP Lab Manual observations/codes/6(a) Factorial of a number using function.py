# Program to print factorial of given number using function

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print("Factorial of value 0:", fact(0))
print("Factorial of value 3:", fact(3))
