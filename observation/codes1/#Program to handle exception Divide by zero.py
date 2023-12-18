#Program to handle exception Divide by zero
try:
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
x=n1/n2
print(n1," / ",n2, " =",x)
y=22/0
print(y)
except ZeroDivisionError:
Result
Thus the program for handling the exception divide by zero executed
successfully.
3. If age>18 print Eligible to vote otherwise print Not Eligible to vote
4. If other than number given , exception ValueError executed and shows Input
must be a number
5. If an I/O error occurs , IOError exception executed and shows IOError
6. Stop.
Ex. No. 10(b)
Date : Exception Handling – Voters Age validity
Aim
To implement program in python for validating voters age and handling the exception.
Algorithm
1. Start
2. Read age of the person
except IOError:
print("IO Error")
#raise ValueError("Invalid age ")
print("Rest of the code ....")
checkvote()
#Multiple exceptions in a try
def checkvote():
try:
age=int(input("Enter your age : "))
if age>18:
print("Eligible to vote")
else:
print("Not Eligible to vote")
except ValueError:
print("Input must be number")
Enter your age : 8
Not Eligible to vote
Rest of the code....
Output
