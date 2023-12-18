# Program to print the items present in a library

# declaring a list of items in a Library
library = ['Books', 'Periodicals', 'Newspaper', 'Manuscripts', 'Maps', 'Prints', 'Documents', 'Ebooks']

# printing the complete list
print('Library:', library)

# printing first element
print('First element:', library[0])

# printing fourth element
print('Fourth element:', library[3])

# printing list elements from 0th index to 4th index
print('Items in Library from 0 to 4 index:', library[0:5])

# printing list -7th or 3rd element from the list
print('3rd or -7th element:', library[-7])

# appending an element to the list
library.append('Audiobooks')
print('Library list after append():', library)
