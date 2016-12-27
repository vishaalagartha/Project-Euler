from itertools import combinations

class Board:
    def __init__(self, n, w):
        self.n = n
        self.w = w
        self.board = []
        for i in range (0, n):
            self.board.append(['O']*n)

    def isValid(self, r, c):
        if 0<=r and r<self.n and 0<=c and c<self.n:
            return True
        return False

    def addQueen(self, r, c):
        if self.board[r][c]!='O':
            return -1
        #queen can move any number of positions horizontally
        for j in range (0, self.n):
            if self.board[r][j]=="Q":
                return -1
            self.board[r][j] = "X"
        #queen can only move n-w-1 positions vertically
        for i in range (0, self.n-self.w):
            if self.isValid(r+i, c):
                if self.board[r+i][c]=="Q":
                    return -1
                self.board[r+i][c] = "X"
            if self.isValid(r-i, c):
                if self.board[r-i][c]=="Q":
                    return -1
                self.board[r-i][c] = "X"
        i=r
        j=c
        while self.isValid(i, j) and abs(i-r)<self.n-self.w and abs(j-c)<self.n-self.w:
            if self.board[i][j]=="Q":
                return -1
            self.board[i][j]="X"
            i+=1
            j+=1
        i=r
        j=c
        while self.isValid(i, j) and abs(i-r)<self.n-self.w and abs(j-c)<self.n-self.w:
            if self.board[i][j]=="Q":
                return -1
            self.board[i][j]="X"
            i-=1
            j+=1
        i=r
        j=c
        while self.isValid(i, j) and abs(i-r)<self.n-self.w and abs(j-c)<self.n-self.w:
            if self.board[i][j]=="Q":
                return -1
            self.board[i][j]="X"
            i+=1
            j-=1
        i=r
        j=c
        while self.isValid(i, j) and abs(i-r)<self.n-self.w and abs(j-c)<self.n-self.w:
            if self.board[i][j]=="Q":
                return -1
            self.board[i][j]="X"
            i-=1
            j-=1
        self.board[r][c]="Q"

        return 0

    def clearBoard(self):
        for i in range (0, self.n):
            for j in range (0, self.n):
                self.board[i][j] = 'O'

    def printBoard(self):
        for i in range (0, self.n):
            print self.board[i]
        print '\n'

def Q(n, w):
    positions = []

    for i in range (0, n):
        for j in range (0, n):
            positions.append([i, j])

    board = Board(n, w)
    counter = 0
    for c in combinations(positions, n):
        i = 0
        r = 0
        while i<n and r!=-1:
            r = board.addQueen(c[i][0], c[i][1])
            if i==n-1 and r!=-1:
                counter+=1
            i+=1
        board.clearBoard()

    return counter

for n in range (1, 6):
    print 'N=', n
    s=0
    for w in range (0, n):
        k = Q(n, w)
        print k
        s+=k

    print 'S=', s
