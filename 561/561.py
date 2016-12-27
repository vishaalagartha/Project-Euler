import numpy as np
from math import sqrt

#fast prime list, good up to 10^8
def ambi_sieve(lim):
    s = np.arange(3, lim, 2)
    for m in xrange(3, int(lim ** 0.5)+1, 2): 
        if s[(m-3)/2]: 
            s[(m*m-3)/2::m]=0
    return list(np.r_[2, s[s>0]])

def prime_factorize(n, primes):
    if n in primes:
        return [n]
    pf = []
    for i in range (2, int(sqrt(n))+1):
        if n%i==0:
            pf=prime_factorize(n/i, primes) + prime_factorize(i, primes)
    return pf

def list_powerset(lst):
        return reduce(lambda result, x: result + [subset + [x] for subset in result],
                                  lst, [[]])


primes = ambi_sieve(10)

temp = prime_factorize(100, primes)
pf = []
for x in set(temp):
    c =temp.count(x)
    for i in range (1, c+1):
        pf.append((x, i))
ps = list_powerset(pf)

divisors = []
for p in ps:
    prod = 1
    for e in p:
        prod*=(e[0]**e[1])
    divisors.append(prod)
print divisors
