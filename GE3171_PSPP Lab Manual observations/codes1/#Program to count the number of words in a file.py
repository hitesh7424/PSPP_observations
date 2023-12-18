#Program to count the number of words in a file
sfile = input("Enter Source File's Name: ")
sourfile=open(sfile, "r")
wcount={}
for line in sourfile:
word_list=line.split()
for word in word_list:
if word not in wcount:
wcount[word]=1
else:
wcount[word]=wcount[word]+1
print("Count of each word in file : ")
print("{:15}{:3}".format("Word","Frequency"))
print("-"*25)
for (word,count) in wcount.items():
print("{:15}{:3}".format(word,count))
Contents of aa.txt
Output
