n = int(input())
P = list(map(int,input().split()))

if P.index(1) == 0 and P.index(n) == n-1:
    print(0)
    exit()

if P.index(1) > P.index(n):
    rev = n-P.index(1) + 2
    jun = P.index(n)+1
    print(min(rev,jun))
else:
    pro = n-P.index(n)+1
    post = P.index(1) + 1 + 1
    print(min(pro,post))