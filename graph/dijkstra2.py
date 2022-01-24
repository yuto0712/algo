import heapq

def dijkstra(M):
    n = len(M)
    color = [-1 for i in range(n)]
    d = [float('inf') for i in range(n)]

    d[0] = 0
    pq = []
    heapq.heappush(pq,(0,0))
    while len(pq) > 0:
        us = heapq.heappop(pq)
        u = us[1]
        color[u] = 1

        if d[u] < us[0]:
            continue

        for v in range(n):
            if color[v] != 1 and M[u][v] != -1:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    color[v] = 0
                    heapq.heappush(pq,(d[v],v))
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
d = dijkstra(M)
for i in range(n):
    print(i,d[i])