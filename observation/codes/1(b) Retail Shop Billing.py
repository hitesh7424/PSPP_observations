# Program to prepare a shopping bill

n = int(input("Enter no. of items purchased: "))
itemname = []
units = []
price = []
totamt = 0

for i in range(1, n + 1):
    item = input("Enter name of the item purchased: ")
    u = int(input("Enter no. of units purchased: "))
    p = int(input("Enter price of the item purchased: "))
    
    itemname.append(item)
    units.append(u)
    price.append(p)

count = len(units)

print("\t\t\t\tXYZ Super Market\n\n")
print("\tItem Name\t\tUnits\tPrice\t\tAmount")

for i in range(count):
    print("\t", itemname[i], "\t\t\t", units[i], "\t", price[i], "\t\t", units[i] * price[i])
    totamt += units[i] * price[i]

print("\n\n\t\t\t\tTotal amount to pay: ", totamt)
print("\n\n\n\t\t\t\tThank You, Visit Again")
