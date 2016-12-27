import numpy as np

#fast prime list, good up to 10^8
def ambi_sieve(lim):
    s = np.arange(3, lim, 2)
    for m in xrange(3, int(lim ** 0.5)+1, 2): 
        if s[(m-3)/2]: 
            s[(m*m-3)/2::m]=0
    return list(np.r_[2, s[s>0]])


def isPrimeTriplet(i, p, mainPrimes, firstPrimes, secondPrimes, thirdPrimes, fourthPrimes):
    for (tp, i1) in secondPrimes:
        if abs(i1-i)<=1:
            for (ttp, i2) in firstPrimes:
                if abs(i2-i1)<=1:
                    return True
            for (mp, i2) in mainPrimes:
                if abs(i2-i1)<=1 and mp!=p:
                    return True
    for (bp, i1) in thirdPrimes:
        if abs(i1-i)<=1:
            for (bbp, i2) in fourthPrimes:
                if abs(i2-i1)<=1:
                    return True
            for (mp, i2) in mainPrimes:
                if abs(i2-i1)<=1 and mp!=p:
                    print (bp, i1), (mp, i2)
                    return True
    for (tp, i1) in secondPrimes:
        if abs(i1-i)<=1:
            for (bp, i2) in thirdPrimes:
                if abs(i2-i)<=1:
                    return True

    return False

def S(row):
    n = row-1

    first = 1+((n-2)*(n-1))/2
    second = 1+((n-1)*(n))/2
    main = 1+(n*(n+1))/2
    third = 1+((n+1)*(n+2))/2
    fourth = 1+((n+2)*(n+3))/2
    fifth = 1+((n+3)*(n+4))/2
    print fifth
    primes = ambi_sieve(fifth+1)

    print "got primes"
    firstPrimes = []
    secondPrimes = []
    mainPrimes = []
    thirdPrimes = []
    fourthPrimes = []
    i=0
    while primes[i]<first:
        i+=1
    print "past first primes"
    while primes[i]<second:
        firstPrimes.append((primes[i], primes[i]-first))
        i+=1
    print "divided first primes"
    while primes[i]<main:
        secondPrimes.append((primes[i], primes[i]-second))
        i+=1
    print "divided second primes"
    while primes[i]<third:
        mainPrimes.append((primes[i], primes[i]-main))
        i+=1
    print "divided main primes"
    while primes[i]<fourth:
        thirdPrimes.append((primes[i], primes[i]-third))
        i+=1
    print "divided third primes"
    while i<len(primes):
        fourthPrimes.append((primes[i], primes[i]-fourth))
        i+=1
    print "divided fourth primes"

    print "divided primes"
    s = 0

    for (p, i) in mainPrimes:
        if isPrimeTriplet(i, p, mainPrimes, firstPrimes, secondPrimes, thirdPrimes, fourthPrimes):
            print p, i
            s+=p




    return s

row = 100000


print S(row)
