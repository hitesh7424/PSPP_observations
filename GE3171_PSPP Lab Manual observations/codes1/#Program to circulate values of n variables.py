#Program to circulate values of n variables
def rotate(listname,nooftimes):
updatelist=listname[nooftimes:]+listname[:nooftimes]
return updatelist
origlist=[]
n=int(input(“Enter no. of items to store in list”))
for i in range(n):
item=int(input(“Enter item value”))
origlist.append(item)
print(“Original list”)
print(origlist)
for i in range(1,len(origlist)):
rotlist=rotate(origlist,i)
print(“rotated list after “,i, “ rotation”,rolist)
Result
Thus the program for circulating the values of n variables executed successfully.
Output
