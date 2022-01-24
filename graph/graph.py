def to_metric(L):
    L = L[2:]
    A = [0 for i in range(n)]
    for idx in L:
        A[idx-1] = 1
    print(*A)

n = int(input())
for _ in range(n):
    L = list(map(int,input().split()))
    to_metric(L)
    