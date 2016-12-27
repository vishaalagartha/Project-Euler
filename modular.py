#returns x such that x is congruent to inv(a) mod b or ax mod b=1 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
    return x1
