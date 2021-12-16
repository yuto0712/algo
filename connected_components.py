from collections import deque
n,m = map(int,input().split())
G = [[] for m in range(n)]
for m in range(m):
    s,t = map(int,input().split())
    G[s].append(t)
    G[t].append(s)

color = [None for i in range(n)]

def dfs(r,c):
    S = deque()
    S.append(r)
    color[r] = c
    while len(S) != 0:
        u = S.pop()
        for i in range(len(G[u])):
            v = G[u][i]
            if color[v] == None:
                color[v] = c
                S.append(v)

def assign_color():
    idx = 1
    for u in range(n):
        if color[u] == None:
            idx += 1
            dfs(u,idx)
assign_color()
q = int(input())
for _ in range(q):
    s,t = map(int,input().split())
    if color[t] == color[s]:
        print('yes')
    else:
        print('no')