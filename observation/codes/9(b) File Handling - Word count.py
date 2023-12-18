# Program to count the number of words in a file

sfile = input("Enter Source File's Name: ")
source_file = open(sfile, "r")
word_count = {}

for line in source_file:
    word_list = line.split()
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

print("Count of each word in the file:")
print("{:15}{:3}".format("Word", "Frequency"))
print("-" * 25)

for word, count in word_count.items():
    print("{:15}{:3}".format(word, count))
