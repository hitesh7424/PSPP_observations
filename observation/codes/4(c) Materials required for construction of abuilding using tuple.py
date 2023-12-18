# Program to store materials required for building construction

building1 = ("bricks", "sand", "cement")
building2 = ("tiles", "paint", "wood", "pipes")

print("Index 1 of building1:", building1[1])
print("Number of components in building1:", len(building1))
print("Number of components in building2:", len(building2))
print("Concatenation of two buildings:", building1 + building2)
print("Repetition of building1:", building1 * 2)
print("Membership operator of building1:", "components" in building1)
print("Membership operator of building2:", "paint" in building2)
print("Slicing of building1:", building1[0:1])
