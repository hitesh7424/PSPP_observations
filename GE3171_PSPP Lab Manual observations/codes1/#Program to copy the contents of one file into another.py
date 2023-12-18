#Program to copy the contents of one file into another
sfile = input("Enter Source File's Name: ")
tfile = input("Enter Target File's Name: ")
sourfile=open(sfile, "r")
destfile= open(sfile, "w")
for line in sourfile:
destfile.write(line)
print("File successfully copied")
I am writing
this file to
check the working
of copy file
Result
Thus the program for copying the contents of one file into another executed
successfully.
sourfile.close()
destfile.close()
print("Contents of destination file")
destfile= open(sfile, "r")
print(destfile.read())
destfile.close()
Output
