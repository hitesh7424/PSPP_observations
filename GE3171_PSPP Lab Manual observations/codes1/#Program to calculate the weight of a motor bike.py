# 1(e) Program to calculate the weight of a motor bike
bikebrand = [
    "TVS Jupiter",
    "Honda Activa",
    "Suzuki Access",
    "Passion Pro",
    "Apache RTR",
]
bikewt = ["109 Kgs", "105 Kgs", "103 Kgs", "118 Kgs", "138 Kgs"]
bn = input("Enter the vehicle name to know the weight")
for i in range(0, len(bikebrand)):
    if bn == bikebrand[i]:
        print("Weight of the Bike ", bikebrand[i], " is ", bikewt[i])
