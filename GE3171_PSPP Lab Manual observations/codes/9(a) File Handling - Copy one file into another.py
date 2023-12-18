# Program to copy the contents of one file into another

sfile = input("Enter Source File's Name: ")
tfile = input("Enter Target File's Name: ")

with open(sfile, "r") as sourfile, open(tfile, "w") as destfile:
    for line in sourfile:
        destfile.write(line)

print("File successfully copied")

# Verify the contents of the destination file
with open(tfile, "r") as destfile:
    print("Contents of destination file:")
    print(destfile.read())

