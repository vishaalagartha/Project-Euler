import numpy as np

#slow primes list, good up to 10^4
def sieve_of_erastothanes(lim):
    primes = range(2, lim+1)
    for p in primes:
        j=2
        while p*j<=lim:
            if p*j in primes:
                primes.remove(p*j)
            j+=1
    return primes

#fast prime list, good up to 10^8
def ambi_sieve(lim):
    s = np.arange(3, lim, 2)
    for m in xrange(3, int(lim ** 0.5)+1, 2): 
        if s[(m-3)/2]: 
            s[(m*m-3)/2::m]=0
    return list(np.r_[2, s[s>0]])
