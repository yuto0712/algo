class CBT():
    def __init__(self,T):
        self.T = T
    
    def parent(self,i):
        if 1 <= i//2 <= len(self.T):
            return self.T[i//2-1]
        else:
            return None
    def left(self,i):
        if 1 <= i*2 <= len(self.T):
            return self.T[i*2-1]
        else:
            return None
    def right(self,i):
        if 1 <= i*2+1 <= len(self.T):
            return self.T[i*2+1-1]
        else:
            return None

n = int(input())
L = list(map(int,input().split()))
CBT = CBT(L)

for i in range(n):
    i += 1
    print(f'node {i}: key = {CBT.T[i-1]},',end = ' ')
    if CBT.parent(i) != None:
        print(f'parent key = {CBT.parent(i)},',end = ' ')
    if CBT.left(i) != None:
        print(f'left key = {CBT.left(i)},',end = ' ')
    if CBT.right(i) != None:
        print(f'right key = {CBT.right(i)},',end = ' ')
    print()
