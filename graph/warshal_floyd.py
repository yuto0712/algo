V,E = map(int,input().split())
D = [[float('INF') for i in range(V)] for _ in range(V)]
for i in range(E):
    s,t,d = map(int,input().split())
    D[s][t] = d

for i in range(V):
    D[i][i] = 0

for k in range(V):
    for i in range(V):
        for j in range(V):
            D[i][j] = min(D[i][j],D[i][k]+D[k][j])
for i in range(V):
    if D[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit()

for d in D:
    out = []
    for item in d:
        if item == float('inf'):
            out.append("INF")
        else:
            out.append(item)
    print(*out)