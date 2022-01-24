def dijkstra(M,s):
    n = len(M)
    color = [-1 for i in range(n)]
    d = [float('inf') for i in range(n)]
    p = [-1 for i in range(n)]
    
    d[s] = 0
    p[s] = -1
    while True:
        mincost = float('inf')
        for i in range(n):
            if color[i] != 1 and d[i] < mincost:
                mincost = d[i]
                u = i

        if mincost == float('inf'):
            break
        
        color[u] = 1
        
        for v in range(n):
            if color[v] != 1 and M[u][v] != -1:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    color[v] = 0
    return d

n = int(input())
M = [[-1]*n for i in range(n)]
for i in range(n):
    line = list(map(int,input().split()))
    idx = line[0]
    m = line[1]
    for j in range(m):
        v,c = line[2+j*2],line[3+j*2]
        M[idx][v] = c
d = dijkstra(M,0)
for i in range(n):
    print(i,d[i])