import numpy

n = 30
M = numpy.matrix([[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]])
x_0 = numpy.matrix([[1], [1], [1], [0], [0], [0]])

print sum(pow(M, n-1)*x_0)
