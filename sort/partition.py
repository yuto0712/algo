def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[j],A[i] = A[i],A[j]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1,A

n=int(input())
L=list(map(int,input().split()))

key,L = partition(L,0,n-1)
L[key] = f'[{L[key]}]'
print(*L)