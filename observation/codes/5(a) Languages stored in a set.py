# Program to print languages stored in a set

langset1 = {"C", "C++", "Java", ".Net", "Python"}
langset2 = {"PHP", "MySQL", "HTML", "Python"}

print("Languages in set 1:", langset1)
print("Languages in set 2:", langset2)
print("Languages in both sets:", langset1 | langset2)
print("Languages common in both sets:", langset1 & langset2)
print("Languages in set 1 but not in set 2 are:", langset1 - langset2)
