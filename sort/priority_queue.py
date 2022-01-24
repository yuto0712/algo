import sys
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
    
    def insert(self,key):
        self.T.append(-float('inf'))
        self.heap_increase_key(len(self.T)-1,key)
    
    def heap_increase_key(self,i,key):
        self.T[i] = key
        while i > 0 and self.T[self.parent(i)] < self.T[i]:
            self.T[self.parent(i)], self.T[i] = self.T[i], self.T[self.parent(i)]
            i = self.parent(i)
    def heap_extract_max(self):
        if len(self.T) == 1:
            return self.T.pop()
        maximum = self.T[0]
        self.T[0] = self.T.pop()
        self.maxheapify(0)
        return maximum

CBT = CBT([])
while True:
    comnum=sys.stdin.readline().split()
    if len(comnum) == 2:
        num = int(comnum[1])
        CBT.insert(num)
    elif comnum[0] == 'end':
        break
    else:
        delnum = CBT.heap_extract_max()
        print(delnum)