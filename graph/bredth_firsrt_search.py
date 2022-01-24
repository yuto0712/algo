from collections import deque

M = []
def to_metric(L,n):
    A = [0 for i in range(n)]
    for idx in L:
        A[idx-1] = 1
    M.append(A)

class Graph():
    def __init__(self,M,n):
        self.color = ['WHITE' for _ in range(n)]
        self.M = M
        self.time = 0
        self.d = [float('inf') for _ in range(n)]
        self.f = [0 for _ in range(n)]
        self.Q = deque()


    def dfs_visit(self,u,n):
        self.time += 1
        self.color[u] = 'GRAY'
        self.d[u] = self.time
        for v in range(n):
            if self.M[u][v] == 0:
                continue
            if self.color[v] == 'WHITE':
                self.dfs_visit(v,n)
        self.color[u] == 'BLACK'
        self.time += 1
        self.f[u] = self.time

    def bfs_visit(self,s,n):
        self.Q.append(s)
        for i in range(n):
            self.d[s] = 0
            while len(self.Q) != 0:
                u = self.Q.popleft()
                for v in range(n):
                    if self.M[u][v] == 0 or self.d[v] != float('inf'):
                        continue
                    self.d[v] = self.d[u] + 1
                    self.Q.append(v)

n = int(input())
for _ in range(n):
    _, _, *L = input().split()
    L = map(int,L)
    to_metric(L,n)
BFS = Graph(M,n)
BFS.bfs_visit(0,n)

for i in range(n):
    if BFS.d[i] == float('inf'):
        BFS.d[i] = -1
    print(i+1,BFS.d[i])
