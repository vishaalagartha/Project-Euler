import numpy

MOD = 10**8
def mod_pow(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y


M = numpy.matrix([[2, 2, -2, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
x_0 = numpy.matrix([[8], [4], [1], [1]])

print (mod_pow(M, 10**12-4, MOD) * x_0)%MOD
