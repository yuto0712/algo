def mcm(n,p):
    m = [[0]*(n+1) for _ in range(n+1)]
    for l in range(2,n+1):  #長さを決める
        for i in range(1,n-l+2):
            j = i+l-1
            m[i][j] = float('inf')
            for k in range(i,j):
                m[i][j] = min(m[i][j],m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j])
    return m[1][n]

n = int(input())
p = []
for i in range(n):
    a,b = map(int,input().split())
    if i == 0:
        p.append(a)
        p.append(b)
    else:
        p.append(b)

print(mcm(n,p))