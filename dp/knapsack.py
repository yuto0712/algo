n,w = map(int,input().split())
V=[]
W=[]
for i in range(n):
    a,b = map(int,input().split())
    V.append(a)
    W.append(b)
dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        # print(i,j)
        if j < W[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            # print(i,j)
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i-1]]+V[i-1])
# print(dp)
print(dp[n][w])