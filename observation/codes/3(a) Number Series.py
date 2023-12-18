# Program to generate a number series

n = int(input("Enter the maximum no. for the series: "))
lst = []

for i in range(1, n + 1):
    print(i, "+ =", end=" ")
    lst.append(i)
    print(sum(lst))
