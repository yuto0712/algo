def prim(M):
    n = len(M)
    color = [-1 for i in range(n)]
    d = [float('inf') for i in range(n)]
    p = [-1 for i in range(n)]
    
    d[0] = 0
    p[0] = -1
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
                if M[u][v] < d[v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = 0
    return d
n = int(input())
M = [list(map(int,input().split())) for i in range(n)]
d = prim(M)
print(sum(d))