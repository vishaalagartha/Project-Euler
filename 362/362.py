def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

N = 100
s = 0
for k in range (2, N+1):
    temp = primes(k)
    primfac = [(i, temp.count(i)) for i in set(temp)]
    l = len(primfac)
    s+=1+(l*(l-1))/2
    print k, 1+(l*(l-1))/2, primfac
print s


