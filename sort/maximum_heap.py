class CBT():
    def __init__(self,T):
        self.T = T
    
    def parent(self,i):
        if 1 <= (i+1)//2 <= len(self.T):
            return (i+1)//2-1
        else:
            return None
    def left(self,i):
        if 1 <= (i+1)*2 <= len(self.T):
            return (i+1)*2-1
        else:
            return None
    def right(self,i):
        if 1 <= (i+1)*2+1 <= len(self.T):
            return (i+1)*2+1-1
        else:
            return None
    def maxheapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l != None and self.T[l] > self.T[i]:
            leargest = l
        else:
            leargest = i
            
        if r != None and self.T[r] > self.T[leargest]:
            leargest = r
        if leargest != i:
            self.T[i],self.T[leargest] = self.T[leargest],self.T[i]
            self.maxheapify(leargest)
    
    def buildmaxheap(self):
        s = len(self.T)//2
        for i in range(s):
            i = s-1-i
            self.maxheapify(i)

n = int(input())
L = list(map(int,input().split()))
CBT = CBT(L)
CBT.buildmaxheap()
print('',*CBT.T)