n = 22
x = []
y = []
for i in range (0, 2*n+1):
    x.append(pow(2, i, n))
    y.append(pow(2, i, n))


print x, y
l = []
for i in range (0, 2*n+1):
    p = (x[i], y[i])
    l.append([])
    for j in range (0, 2*n+1):
        if p[0]<=x[j] and p[1]<=y[j] and p!=(x[j], y[j]):
            l[i].append((x[j], y[j]))


print l
