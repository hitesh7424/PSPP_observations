# Program to print maximum element in the list

def maxi(n):
    mx = n[0]
    for i in range(1, len(n)):
        if n[i] > mx:
            mx = n[i]
    return mx

nos = int(input("Enter no. of elements to store: "))
num = []

for i in range(0, nos):
    inp = int(input("Enter a number: "))
    num.append(inp)

print("Elements stored in the list are:")
print(num)
m = maxi(num)
print("Maximum value stored in the list:", m)
