from collections import deque

class LFG(object):
    def __init__(self):
        self.k = 1
        self.history = [0]*55

    def next(self):
        k = self.k
        if k<=55:
            res = (100003-200003*k+300007*k*k*k)%1000000
            self.k+=1
        else:
            res = (self.history[-24]+self.history[-55])%1000000
        del self.history[0]
        self.history.append(res)
        return res


def BFS(A, x):
    n = len(A)
    connected = 0
    visited = [False]*n
    q = deque([x])

    while not q:
        s = q.popleft()
        for i in A[s]:
            if not visited[i]:
                connected+=1
                visited[i] = True
                q.append(i)
    return float(connected)/n

        


s_k = deque([])
pm = 524287
A = dict()
for k in range(1, 56):
    s_k.append((100003-200003*k+300007*k**3)%1000000)
    if k%2==0:
        p = s_k[k-2]
        q = s_k[k-1]
        if p not in A:
            A[p] = []
        if q not in A:
            A[q] = []
        A[p].append(q)
        A[q].append(p)

k = 56
connectedness = BFS(A, pm)
while connectedness==0:
    if k%1000000==0:
        print k
    s = (s_k[0]+s_k[31])%1000000
    s_k.popleft()
    s_k.append(s)
    if k%2==0:
        p = s_k[-2]
        q = s_k[-1]
        if p!=q:
            if p not in A:
                A[p] = []
            if q not in A:
                A[q] = []
            A[p].append(q)
            A[q].append(p)
    k+=1
    connectedness = BFS(A, pm)
