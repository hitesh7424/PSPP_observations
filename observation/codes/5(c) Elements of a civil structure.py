# Program to store elements of a civil structure using dictionary

ele = {
    "Foundation": "Spread footing",
    "Column": "Structural",
    "Roof": "Flat",
    "Lintel": "RCC",
    "Doors": "Teak Wood",
    "Window": "Rose Wood",
    "Wall": "Bricks",
}

print("Elements of a civil structure are:")
print(ele)

ele["Floor"] = "Tiles"
print("\nElements after adding floor:")
print(ele)

ele["Roof"] = "Sloped"
print("\nElements after changing roof value:")
print(ele)

del ele["Window"]
print("\nElements after deleting component Window:")
print(ele)
