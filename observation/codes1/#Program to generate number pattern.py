#Program to generate number series
n=int(input(“Enter the maximum no. for the series : ”))
lst=[]
for i in range(1,n+1):
print(i,”+ =”,end=” “)
lst.append(i)
print(sum(lst))
Result
Thus the number series for the given range printed successfully.
Ex. No. 3(b)
Number Pattern
Date :
Aim
To print the number pattern based on the input given by the user.
Algorithm
1. Start
2. Read maximum number for the series n
3. Initialize the value of i as 1 and j as 1.
4. Print the number pattern with the value of i printed j times
5. Repeat the step 4 till it reaches n+1
6. Print the number pattern with the value of j printed i times
7. Repeat the step 6 till it reaches n+1
8. Stop
print("Number pattern 2")
for i in range(1,n+1):
for j in range(1,i+1):
print(j," ",end=" ")
print("\n")
#Program to generate number pattern
n=int(input("Enter the maximum no. for the series : "))
print("Number pattern 1")
for i in range(1,n+1):
for j in range(1,i+1):
print(i," ",end=" ")
print("\n")
Output
