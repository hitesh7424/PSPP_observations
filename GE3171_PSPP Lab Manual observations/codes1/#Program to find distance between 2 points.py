#Program to find distance between 2 points
Distance=√(X2-X1)
2+(Y2-Y1)
2
import math
x1=int(input("Enter values for x1 : "))
y1=int(input("Enter values for y1 : "))
x2= int(input("Enter values for x2 : "))
y2= int(input("Enter values for y2 : "))
dist=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(dist)
Enter values for y2 : 30
10.198039027185569
Result
Thus the distance between 2 points computed successfully.
Ex. No. 3(a)
Number Series
Date :
Aim
To generate a number series upto a given number.
Algorithm
1. Start
2. Read maximum number for the series n
3. Initialize the value of i as 1 and create an empty list lst.
4. Print value of i and append the i value to lst
5. Print the sum.
6. Repeat the step 4 , 5 till it reaches n+1
7. Stop
Output
