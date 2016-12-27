
def det(a, b, c, d):
    return a*d-b*c

def liesIn(p, p1, p2):
    if p[0]>min(p1[0], p2[0]) and p[0]<max(p1[0], p2[0]):
        return True
    if p[1]>min(p1[1], p2[1]) and p[1]<max(p1[1], p2[1]):
        return True
    return False


def intersectionPoint((x1, y1), (x2, y2), (x3, y3), (x4, y4), l):
        d = det(x1-x2, y1-y2, x3-x4, y3-y4)
        if d==0:
            return 0
        d1 = det(x1, y1, x2, y2)
        d2 = det(x3, y3, x4, y4)

        n_x = det(d1, x1-x2, d2, x3-x4)
        n_y = det(d1, y1-y2, d2, y3-y4)

        a, b = float(n_x)/d, float(n_y)/d
        if liesIn((a, b), (x1, y1), (x2, y2)) and liesIn((a, b), (x3, y3), (x4, y4)):
            l+=[(a, b)]

p = []
i=0
s = 290797
while i<=20000:
    s = s**2 % 50515093
    p.append(s % 500)
    i+=1

l = []
intersections = 0
for i in range (0, len(p)-8, 4):
    print i
    for j in range(i+4, len(p)-4, 4):
        intersectionPoint((p[i], p[i+1]), (p[i+2], p[i+3]), (p[j], p[j+1]), (p[j+2], p[j+3]), l)

print len(set(l))
