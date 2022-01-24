from collections import deque


h,w = map(int,input().split())

grid = [input() for i in range(h)]

dist = [[-1]*w for _ in range(h)]

black_cells = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            black_cells.append((i,j))
            dist[i][j] = 0

d = 0
while black_cells:
    i,j = black_cells.popleft()
    d = dist[i][j]
    for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
        new_i = i + dx
        new_j = j + dy
        if new_j < 0 or new_j >= w or new_i < 0 or new_i >= h:
            continue
        if dist[new_i][new_j] == -1:
            dist[new_i][new_j] = d+1
            black_cells.append((new_i,new_j))

print(d)