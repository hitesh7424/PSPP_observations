# Program to replace characters in a string

str1 = input("Enter a string: ")
print("String given as input:", str1)

# Replace the first occurrence of 'a' with 'v'
print("String replaced with the given character only once:")
changed_str_once = str1.replace("a", "v", 1)
print("The changed string is:", changed_str_once)

# Replace up to 3 occurrences of 'a' with 'v'
print("String replaced with the given character up to 3 occurrences:")
changed_str_three_times = str1.replace("a", "v", 3)
print("The changed string is:", changed_str_three_times)
