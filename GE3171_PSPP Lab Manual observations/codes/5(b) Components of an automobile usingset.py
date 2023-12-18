# Program to print components of an automobile using set

carcomp = {"chassis", "engine", "suspension", "axle", "doors", "Wiper", "fuel tank"}
print("Components of a car are:", carcomp)

bikecomp = {"engine", "brake", "fuel tank"}
print("Components of a bike are:", bikecomp)

print("\nComponents common to car and bike are:")
print(carcomp & bikecomp)

print("\nComponents of car and bike combined are:")
print(carcomp | bikecomp)

print("\nComponents of car but not for bike are:")
print(carcomp - bikecomp)
