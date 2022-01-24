h,w = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(h)]

dp = [[0 for _ in range(w)] for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if C[i][j] == 1:
            dp[i][j] = 0
        else:
            if i==0:
                dp[0][j] = 1
            elif j==0:
                dp[i][0] = 1
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
        ans = max(ans,dp[i][j])
print(ans**2)