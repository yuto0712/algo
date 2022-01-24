from collections import deque, defaultdict
Tree = defaultdict(lambda: [])

# input data
N = int(input())
for _ in range(N - 1):
    s, t, w = list(map(int, input().split()))
    Tree[s].append((t, w))
    Tree[t].append((s, w))

def bfs(Tree, N, s):
    dist = [float('inf') for _ in range(N)]
    que = deque([(s,0)])
    seen = [False for _ in range(N)]
    seen[s] = True
    while que:
        cur, cost = que.popleft()
        dist[cur] = cost
        for node, w in Tree[cur]:
            if seen[node]:
                continue
            que.append((node, w+cost))
            seen[node] = True
    return dist

dist = bfs(Tree, N, 0)
idx = dist.index(max(dist))
dist = bfs(Tree, N, idx)
print(max(dist))