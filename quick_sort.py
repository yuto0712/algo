def partition(A,p,r,B):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[j],A[i] = A[i],A[j]
            B[j],B[i] = B[i],B[j]
    A[r],A[i+1] = A[i+1],A[r]
    B[r],B[i+1] = B[i+1],B[r]
    return i+1

def quicksort(A,p,r,B):
    if p < r:
        q = partition(A,p,r,B)
        quicksort(A,p,q-1,B)
        quicksort(A,q+1,r,B)

n = int(input())
N=[]
G=[]
B=[]
M=[]
for i in range(n):
    a,b = map(str,input().split())
    N.append(int(b))
    G.append(int(b))
    B.append(a)
    M.append(a)


def merge(A,left,mid,right,cnt,M):
    n1=mid-left
    n2=right-mid
    L = A[left:mid]
    R = A[mid:right]
    Lm = M[left:mid]
    Rm = M[mid:right]# print(left,right)
    # print(L,R)
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            M[k] = Lm[i]
            i += 1
            cnt += 1
        else:
            A[k] = R[j]
            M[k] = Rm[j]
            j += 1
            cnt += 1
    return cnt

def merge_sorted(A,left,right,cnt,M):
    if left+1 < right:
        mid = (left+right)//2
        cnt = merge_sorted(A,left,mid,cnt,M)
        cnt = merge_sorted(A,mid,right,cnt,M)
        cnt = merge(A,left,mid,right,cnt,M)
    return cnt

quicksort(N,0,n-1,B)
cnt=0
cnt = merge_sorted(G,0,n,cnt,M)
if B==M:
    print('Stable')
else:
    print('Not stable')

for i in range(n):
    print(B[i],N[i])