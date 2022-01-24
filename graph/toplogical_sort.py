import queue

V,E = map(int,input().split())
G =[[] for i in range(V)]
indeg = [0 for i in range(V)]

for i in range(E):
    s,t = map(int,input().split())
    indeg[t] += 1
    G[s].append(t)

def topological_sort_bfs():
    out = []
    color = ['WHITE' for i in range(V)]
    Q = queue.Queue()
    for u in range(V):
        if color[u] == 'WHITE' and indeg[u] == 0:
            bfs(u,Q,color,out)
    return out

def bfs(s,Q,color,out):
    Q.put(s)
    color[s] = 'GRAY'
    while not Q.empty():
        u = Q.get()
        out.append(u)
        for v in G[u]:
            indeg[v] -= 1
            if indeg[v] == 0 and color[v] == 'WHITE':
                color[v] = 'GRAY'
                Q.put(v)

def topological_sort_dfs():
    out = []
    color = ['WHITE' for i in range(V)]
    for u in range(V):
        if color[u] == 'WHITE':
            dfs(u,color,out)
    return out
def dfs(s,color,out):
    color[s] = 'GRAY'
    for v in G[s]:
        if color[v] == 'WHITE':
            dfs(v,color,out)
    out.append(s)

out = topological_sort_dfs()
out.reverse()
for item in out:
    print(item)