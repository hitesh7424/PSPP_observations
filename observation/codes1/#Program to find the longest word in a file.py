#Program to find the longest word in a file
sfile = input("Enter Source File's Name: ")
sourfile=open(sfile, "r")
wcount={}
maxi=0
noofwords=0
for line in sourfile:
word_list=line.split()
for word in word_list:
if word not in wcount:
Output
