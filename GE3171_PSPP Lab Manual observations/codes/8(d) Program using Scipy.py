# Program using scipy module to find determinant of the matrix

from scipy import linalg
import numpy as np

two_darray = np.array([[4, 5], [3, 2]])
result = linalg.det(two_darray)
print(result)
