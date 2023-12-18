# Program using numpy module

import numpy as np

a = np.array([(8, 9, 10), (11, 12, 13)])

print("Original Dimension of the array:")
print(f"Shape: {a.shape}")
print(a)

print("\nModified Dimension of the array:")
a = a.reshape(3, 2)
print(f"Shape: {a.shape}")
print(a)
