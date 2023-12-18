#Program to print components of an automobile using set
carcomp={"chassis","engine","suspension","axle","doors","Wiper","fuel tank"}
print("components of a car are ",end="")
print(carcomp)
bikecomp={"engine","brake","fuel tank"}
print("components of a bike are ",end="")
print(bikecomp)
print("components common to car and bike are ")
print(carcomp&bikecomp)
print("components of car and bike combined are ")
components of car and bike combined are
{'suspension', 'Wiper', 'engine', 'doors', 'chassis', 'axle', 'brake', 'fuel tank'}
components of car but not for bike are
{'Wiper', 'suspension', 'doors', 'chassis', 'axle'}
Result
Thus components of automobile car and bike are stored in sets and executed
using different set operations.
Ex. No. 5(c)
Elements of a civil structure
Date :
Aim
To demonstrate dictionary operations by storing the elements of a civil
structure.
Algorithm
1. Start
2. Create a dictionary ele with 7 elements of key and value.
3. Print contents in the dictionary
4. Add a new key floor and print the dictionary content
5. Change the value of the key floor and print the updated content in the dictionary
6. Remove the key window and show updated content
7. Stop
print("Elements after changing roof value ")
print(ele)
del ele["Window"]
print("Elements after deleting component window ")
print(ele)
#Program to store elements of a civil structure using dictionary
ele={"Foundation":"Spreadfooting","Column":"structural","roof":"flat","Lintel":"RCC","d
oors":"Teak Wood","Window":"Rose wood","wall":"bricks"}
print("Elements of a civil structure are : ")
print(ele)
ele["floor"]="Tiles"
print("Elements after adding floor")
print(ele)
ele["roof"]="sloped"
Output
