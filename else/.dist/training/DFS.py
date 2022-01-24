from collections import deque
import sys
sys.setrecursionlimit(10**7)

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int,input().split())) for _ in range(h)]

    que = deque()

    seen = [[-1]*w for _ in range(h)]
    colors =[[0]*w for _ in range(h)]

    def dfs(x, y,color):
        # 範囲外や壁の場合は終了
        # # 確認したルートは壁にしておく
        if y >= w or y < 0 or x >= h or x < 0 or grid[x][y] == 0 or seen[x][y] == 0:
            return
        
        seen[x][y] = 0
        colors[x][y] = color
        # 上下左右への移動パターンで再起していく
        dfs(x+1, y, color)
        dfs(x-1, y, color)
        dfs(x, y+1, color)
        dfs(x, y-1, color)
        dfs(x-1, y-1, color)
        dfs(x+1, y-1, color)
        dfs(x+1, y+1, color)
        dfs(x-1, y+1, color)

    color = 0
    for i in range(h):
        for j in range(w):
            if seen[i][j] == 0 or grid[i][j] == 0:
                continue
            else:
                color += 1
                dfs(i,j,color)

    ans = 0
    for i in range(h):
        ans = max(ans,max(colors[i]))
    print(ans)
