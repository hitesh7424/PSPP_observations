# Program to store spare parts required to assemble a car

car1 = ("steering", "wheels", "brake", "engine", "seats")
car2 = ("accelerator", "clutch", "gear", "horn", "indicator", "battery")

print("Indexing position of car2:", car2[1])
print("Number of components in car1:", len(car1))
print("Number of components in car2:", len(car2))
print("Concatenation of two cars:", car1 + car2)
print("Repetition of car1:", car1 * 2)
print("Membership operator of car1:", "engine" in car1)
print("Membership operator of car2:", "components" not in car2)
print("Slicing of car2:", car2[0:2])
