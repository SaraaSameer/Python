import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr1 = arr[::-1]
    return numpy.array(arr1)


arr = [1, 2, 3, 4, 5]
result = arrays(arr)
result = result.astype("float64")
print(result)