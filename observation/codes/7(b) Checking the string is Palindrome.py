# 7(c) Program to check given string is palindrome
str1 = input("Enter a string : ")

if str1 == str1[::-1]:
    print("String entered '{}' is a palindrome".format(str1))
else:
    print("String entered '{}' is not a palindrome".format(str1))
