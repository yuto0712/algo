M = []
def to_metric(L,n):
    A = [0 for i in range(n)]
    for idx in L:
        A[idx-1] = 1
    M.append(A)

class DFS():
    def __init__(self,M,n):
        self.color = ['WHITE' for _ in range(n)]
        self.M = M
        self.time = 0
        self.d = [0 for _ in range(n)]
        self.f = [0 for _ in range(n)]

    def dfs_visit(self,u,n):
        self.time += 1
        self.color[u] = 'GRAY'
        self.d[u] = self.time
        for v in range(n):
            if self.M[u][v] == 0:
                continue
            if self.color[v] == 'WHITE':
                self.dfs_visit(v,n)
        self.color[u] = 'BLACK'
        self.time += 1
        self.f[u] = self.time

n = int(input())
for _ in range(n):
    _, _, *L = input().split()
    L = map(int,L)
    to_metric(L,n)
DFS = DFS(M,n)
for u in range(n):
    if DFS.color[u] == 'WHITE':
        DFS.dfs_visit(u,n)

for i in range(n):
    print(i+1,DFS.d[i],DFS.f[i])