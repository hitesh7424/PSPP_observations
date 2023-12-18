# Program to generate number pattern

n = int(input("Enter the maximum no. for the series: "))

print("Number pattern 1")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, " ", end=" ")
    print("\n")

print("Number pattern 2")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, " ", end=" ")
    print("\n")
