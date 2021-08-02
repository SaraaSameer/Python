import numpy as np

# Output [[1 1 1 1 1]
#         [1 0 0 0 1]
#         [1 0 9 0 1]
#         [1 0 0 0 1]
#         [1 1 1 1 1]]

# Method 01
arr = np.ones((5, 5))
arr[1:4, 1:4] = 0
arr[2, 2] = 9
print(arr)
print("")
print("")

# Method 02
arr1 = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9

arr1[1:-1, 1:-1] = z
print(arr1)


