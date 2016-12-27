from math import log
def printDP(a, b, dp):
    temp = list(b)
    temp = map(int, temp)
    print '    ', temp
    print ' ', dp[0]
    for i in range (1, n+1):
        print a[i-1], dp[i]

def sieve(n):
    primes = range(2, n+1)
    for p in primes:
        j = 2
        while p*j<n:
            if p*j in primes:
                primes.remove(p*j)
            j+=1
    return primes

def digitalRoot(n):
    s = str(n)
    while len(s)>1:
        s = str(sum(int(k) for k in str(s)))

    return s

n = 10
lim = n*(log(n)+log(log(n))) 
primes = sieve(int(lim))

primeC=0
compositeC=0
k=2
a = ''
b = ''
while primeC<n or compositeC<n:
    if primeC<n and k in primes:
        a+=digitalRoot(k)
        primeC+=1
    elif compositeC<n and k not in primes:
        b+=digitalRoot(k)
        compositeC+=1
    k+=1

#print a, b
dp = []
for i in range (0, n+1):
    dp.append([])
    for j in range (0, n+1):
        if i==0 or j==0:
            dp[i].append(0)
        elif a[i-1]==b[j-1]:
            dp[i].append(dp[i-1][j-1]+1)
        else:
            dp[i].append(max(dp[i-1][j], dp[i][j-1]))

seq = ''
i = n
j = n
printDP(a, b, dp)
mod = 10**9+7
while i>0 and j>0:
    print i, j
    #print i, j, dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i][j-1]
    #Case 1: all four equal, pick minimum one
    if dp[i][j]==dp[i-1][j-1]:
        seq+=max(a[i-1], b[j-1])
        if a[i-1]>b[j-1]:
            i-=1
        else:
            j-=1
    #Case 2: diagonal equal, pick either one
    elif dp[i-1][j]==dp[i][j-1] and dp[i][j]-1==dp[i-1][j-1]:
        #print 'overlap'
        seq+=max(a[i-1], b[j-1])
        i-=1
        j-=1
    #Case 3: moving left in dp table
    elif dp[i][j-1]==dp[i][j]:
        seq+=b[j-1]
        j-=1
    #Case 4: moving up in dp table
    elif dp[i-1][j]==dp[i][j]:
        seq+=a[i-1]
        i-=1
    print int(seq[::-1])%mod
    #seq = str(int(seq[::-1])%mod)[::-1]

if i==0:
    seq = b[0:j]+seq[::-1]
else:
    seq = a[0:i]+seq[::-1]

print seq
print int(seq)%mod
