#Program to print pyramid pattern
r=int(input("Enter no.of.rows:"))
k=0
for i in range(1,r+1):
for space in range(1,(r-i)+1):
print(end="")
while k!=(2*i-1):
print("*",end="")
k+=1
k=0
print()
*********
Result
The character pattern in pyramid format printed successfully
Ex. No. 4(a)
Items present in a library using list
Date :
Aim
To print the items present in a library using different list operations.
Algorithm
1. Start
2. Create a list in the name library and store the elements in it.
3. Print the entire list using print function.
4. Print the 1
st element and the 4
th element using index number of the list.
5. Print elements from index 0 to 4
6. Add a new element in the list using append function
7. Print the updated list of items in the library
8. Stop
#Program to print the items present in a library
# declaring a list of items in a Library
library=['Books','Periodicals','Newspaper','Manuscripts','Maps','Prints','Documents','Ebooks
']
# printing the complete list
print('Library: ',library)
# printing first element
print('first element: ',library[0])
# printing fourth element
print('fourth element: ',library[3])
# printing list elements from 0th index to 4th index
print('Items in Library from 0 to 4 index: ',library[0: 5])
# printing list -7th or 3rd element from the list
print('3rd or -7th element: ',library[-7])
# appending an element to the list
library.append('Audiobooks')
print('Library list after append(): ',library)
Output
