def P(n):
    if n==1:
        return 1
    if n==2 or n==3:
        return 2
    ret = P(n/4)*4
    if n%4<2:
        ret-=2
    return ret

def S(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 3
    if n==3:
        return 5
    MOD = 987654321
    x = n/4
    ret = (S(x-1) * 16) % MOD - ((x-1) * 4) % MOD + 5
    for y in range (x*4, n+1):
        ret+=P(y)%MOD
    return (ret+MOD)%MOD

print S(pow(10, 18))
