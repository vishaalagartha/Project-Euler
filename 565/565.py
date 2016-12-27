import numpy as np
from itertools import combinations

#fast prime list, good up to 10^8
def ambi_sieve(lim):
    s = np.arange(3, lim, 2)
    for m in xrange(3, int(lim ** 0.5)+1, 2): 
        if s[(m-3)/2]: 
            s[(m*m-3)/2::m]=0
    return list(np.r_[2, s[s>0]])

n = 20
primes = ambi_sieve(n)

for p in primes:
    exp = 0
    temp = primes[:]
    temp.remove(p)
    print temp
    while p**exp<=n:
        t = (p**(exp+1)-1)/(p-1)
        if t%7==0:
            print p**exp, t
        exp+=1

