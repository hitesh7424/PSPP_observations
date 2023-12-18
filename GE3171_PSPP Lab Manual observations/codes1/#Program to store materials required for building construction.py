#Program to store materials required for building construction
building1=("bricks","sand","cement")
building2=("tiles","paint","wood","pipes")
print("Index 1 of building1 : ",building1[1])
print("Numbers of components in building1 : ",len(building1))
print("Numbers of components in building2 : ",len(building2))
print("Concatenation of two building ",building1+building2)
print("Repetition of building1 ",building1*2)
Membership operator of building1: False
Membership operator of building2: True
Slicing of building1: ('bricks',)
Result
Materials required for construction of a building are stored and printed using
different tuple operations executed.
print("Membership operator of building1: ","components" in building1)
print("Membership operator of building2: ","paint" in building2)
print("Slicing of building1:",building1[0:1])
Output
