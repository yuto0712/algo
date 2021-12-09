n,k=map(int,input().split())
L=[]
for j in range(n):
    a=int(input())
    L.append(a)

def load(p):
    if p < max(L):
        return False
    w=0
    i=0
    track = 1
    for i in range(n):
        w+=L[i]
        if w > p:
            track+=1
            if track > k:
                return False
            w=L[i]
    return True
# print(load(6))

left = 0
right = 10**9
while left < right:
    mid = (left+right)//2
    # print(f'mid{mid}')
    if load(mid):
        right = mid
        tmp = mid
    else:
        left = mid + 1
        if left >= right:
            break
print(tmp)

