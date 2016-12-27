a = 1777
k = 1855
mod = 10**8
p = pow(a, a, mod)
for i in range (2, k):
    p = pow(a, p, mod)

print p

    
