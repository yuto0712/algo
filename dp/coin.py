n,m = map(int,input().split())
c = list(map(int,input().split()))

dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0
# print(dp)
for i in range(1,m+1):
    for j in range(1,n+1):
        # print(i,j)
        if j < c[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-c[i-1]]+1)

print(dp[m][n])