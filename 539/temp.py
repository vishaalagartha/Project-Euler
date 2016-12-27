

N=pow(10, 4)

forwards = [0, 1, 2]
backwards = [0, 1, 1]
fs = [0, 1, 3]
bs = [0, 1, 2]

for i in range(3, N+1):
    if i%2==0:
        forwards.append(backwards[i/2]*2)
    else:
        forwards.append(forwards[i-1])
    backwards.append(i-forwards[-1]+1)
    fs.append(fs[-1]+forwards[-1])
    bs.append(bs[-1]+backwards[-1])

i = 0
while 2**i<len(fs):
    print 2**i, forwards[2**i]
    i+=1

k = 7
s = (bin(k)[2:])[::-1]
print s
for i in range (0, len(s)):
    if s[i]=='1':
        print 2**i, forwards[2**i]
print forwards[k]
