#Program using numpy module
import numpy as np
a = np.array([(8,9,10),(11,12,13)])
print("Original Dimension of the array : ",a.shape)
print(a)
print("Modified Dimension of the array : ",end="")
a=a.reshape(3,2)
print(a.shape)
print(a)
[10 11]
[12 13]]
Result
Thus the program numpy with array executed successfully.
3. Store in text=["IBM","Amazon","Facebook","Microsoft","Google"]
4. Store in colors=["red","orange","yellow","blue","green"]
5. Using xlim() and ylim() we can set the points as 0 to 6 on x-axis and 0 to100 on yaxis respectively.
6. Using bar() we can create a bar graph with x,y with label as text andcolor=colors
and line width of the graph as 0.5.
7. show the x-axis and y-axis of the plot as ‘Company' and 'Percentage',show the title
as Percentage Graph.
Ex. No. 8(c)
Date : Program using matplotlib
Aim
To implement program in python for working with matplotlib to plot charts.
Algorithm
1. Store in x=[1,2,3,4,5]
2. Store in y=[50,65,85,87,98]
#Program to plot a chart using matplotlib module
import matplotlib.pyplot as mpl
x=[1,2,3,4,5]
y=[50,65,85,87,98]
text=["IBM","Amazon","Facebook","Microsoft","Google"]
colors=["red","orange","yellow","blue","green"]
mpl.xlim(0,6)
mpl.ylim(0,100)
mpl.bar(x,y,tick_label=text,color=colors,linewidth=0.5)
mpl.xlabel("Company")
mpl.ylabel("Percentage")
mpl.title("Percentage Graph")
mpl.show()
Output
