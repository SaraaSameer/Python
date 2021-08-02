import numpy

arr = numpy.ones(9)
a = input()
a = a.split(' ')
arr = numpy.array(a)
print(numpy.reshape(arr, (3, 3)))
