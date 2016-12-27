#returns phi(n)
import fractions

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

#returns list of phi values from 1 to n
def totientsList(n):
    phi = range(1, n+1)
    for i in range(2, n + 1):
        if phi[i] != i:
            continue
        for j in range(i, n + 1, i):
            phi[j] = phi[j] // i * (i - 1)
