#Program to compute electric current in 3 phase AC circuit
v=int(input(“Enter the voltage of the AC Circuit”))
c=int(input(“Enter the current value of the AC Circuit”))
pf=float(input(“Enter the power factor of the AC Circuit”))
ec=√3*v*c*pf
print(“Electric current in 3 phase AC circuit”,ec)
Result
Thus the program for computing electric current in 3 phase AC circuit executed
successfully.
Ex. No. 2(a)
Exchange the values of two variables
Date :
Aim
To write a python program to exchange values of 2 variables
Algorithm
1. Start
2. Read 2 numbers as a and b
3. print the values got from user
4. call the function swap by passing the 2 parameters a and b
5. Assign the value of a to b and b to a
6. print the values after exchange
7. Stop
#Program to exchange the value of 2 variables
def swap(a,b):
a,b=b,a
print(“After swapping”)
print(“Value of a = “,a, “ and value of b = “,b)
a=int(input(“Enter first number”))
b=int(input(“Enter second number”))
After swapping
Value of a = 45 and value of b = 25
Result
Thus the values of 2 variables exchanged successfully.
print(“Before swapping”)
print(“Value of a = “,a, “ and value of b = “,b)
swap(a,b)
Output
