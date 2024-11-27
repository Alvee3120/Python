import numpy as np

# 1. Creating a basic NumPy array
array_1d = np.array([1, 2, 3, 4, 5])  # 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

print("1D Array:")
print(array_1d)
print("\n2D Array:")
print(array_2d)

# 2. Basic Array Operations
# Element-wise addition
array_add = array_1d + 5
print("\nElement-wise Addition:")
print(array_add)

# Element-wise multiplication
array_multiply = array_1d * 2
print("\nElement-wise Multiplication:")
print(array_multiply)

print("\nMaximum value in 1D array:", array_1d.max())
print("Minimum value in 1D array:", array_1d.min())
print("Sum of all elements in 1D array:", array_1d.sum())
print("Mean of all elements in 1D array:", array_1d.mean())

# 4. Array Indexing and Slicing
print("\nFirst element of 1D array:", array_1d[0])
print("Elements from index 1 to 3 in 1D array:", array_1d[1:4])

# Slicing a 2D array (extracting the first row)
print("\nFirst row of 2D array:")
print(array_2d[0, :])
