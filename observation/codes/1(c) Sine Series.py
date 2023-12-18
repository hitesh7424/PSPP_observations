# Program to find the sum of sine series x - x^3/3! + x^5/5! + ...

x = int(input("Enter value of x: "))
n = int(input("Enter value for n: "))
sign = -1
fact = i = 1
sum = 0

while i <= n:
    p = 1
    fact = 1
    for j in range(1, i * 2):
        p = p * x
        fact = fact * j
        # print(p," ",fact)
    sign = -1 * sign
    sum = sum + sign * p / fact
    i = i + 1

print("Sin(", x, ") = ", sum)
