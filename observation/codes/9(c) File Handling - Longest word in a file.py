# Program to find the longest word in a file

sfile = input("Enter Source File's Name: ")
source_file = open(sfile, "r", encoding="utf-8")
word_count = {}
max_length = 0
longest_word = ""
no_of_words = 0

for line in source_file:
    word_list = line.split()
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
            leng = len(word)
            if leng > max_length:
                max_length = leng
                longest_word = word
        else:
            word_count[word] += 1
        no_of_words += 1

source_file.close()
print("Words and their occurrences in the file:")
print(word_count)
print("Number of words in the file:", no_of_words)
print("Longest word:", longest_word)
