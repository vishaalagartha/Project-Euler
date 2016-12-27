def translate(w):
    alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 8}
    d = {}
    l = []

    for c in w:
        if alphabet[c] not in d:
            d[alphabet[c]]=0
        d[alphabet[c]]+=1
        l.append(alphabet[c])
    return d, l


def position(w, d, l):
    w = translate(w)[1]
    print w, d

    keys = sorted(d.keys())
    n = 0
    print keys
    for c in w:
        index = keys.index(c)
        print index
        
        print c


string = 'data'
l = 3


d = translate(string)[0]
print position('ada', d, l)
