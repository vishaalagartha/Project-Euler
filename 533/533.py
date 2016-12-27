from totient import phi
from gcd import gcd
from math import sqrt, floor
from sys import argv

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def carmichael(n):
    pf = fac(n)
    p_dict = dict()
    for p in pf:
        if p not in p_dict:
            p_dict[p]=0
        p_dict[p]+=1
    prime_powers = [p**p_dict[p] for p in p_dict]
    pp_lambda = []
    
    print prime_powers
    for v in prime_powers:
        temp = v
        if temp==2:
            pp_lambda.append(1)
        elif temp==4:
            pp_lambda.append(2)
        else: #it is a power of an odd prime 
            pp_lambda.append(phi(v))

    return lcmm(pp_lambda)


print carmichael(100)
