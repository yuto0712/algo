def merge(A,left,mid,right,cnt):
    n1=mid-left
    n2=right-mid
    L = A[left:mid]
    R = A[mid:right]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            cnt += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += 1
    return cnt

def merge_sorted(A,left,right,cnt):
    if left+1 < right:
        mid = (left+right)//2
        cnt = merge_sorted(A,left,mid,cnt)
        cnt = merge_sorted(A,mid,right,cnt)
        cnt = merge(A,left,mid,right,cnt)
    return cnt
cnt = 0
n=int(input())
L=list(map(int,input().split()))

cnt = merge_sorted(L,0,n,cnt)
print(*L)
print(cnt)
