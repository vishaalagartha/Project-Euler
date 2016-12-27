def sumflsq(n):
    return isqrt(n) * (n - (2 * isqrt(n) + 5)*(isqrt(n) - 1) / 6)

def T(n):
    arr = [1]
    while sum(arr) < n:
        parr = copy(arr)
        parr.append(0)
        arr.append(1)
        l = len(arr)
        s = 0
        for i in range(1,l):
            s += sumflsq(arr[l - i]) - sumflsq(parr[l - i])
            arr[l - i - 1] += s

    if sum(arr) == n:
        return sum([a*(a + 1)/2 for a in s])

    arr = parr
    j = len(arr) - 2
    arr[j + 1] = 1    
    while j >= 0:
        while sum(arr) < n:
        parr = copy(arr)
        arr[j] += 1
        s = 0
        for i in range(1,j + 1):
        s += sumflsq(arr[j - i + 1]) - sumflsq(parr[j - i + 1])
        arr[j - i] += s    
        if sum(arr) == n:
        return sum([a*(a + 1)/2 for a in arr])
        arr = parr
        j -= 1

T(10^18)
