def counting_sort(A,B,k):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(k+1)]
    for j in range(n):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for i in range(n):
        j = n-1-i
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B
n = int(input())
A = list(map(int,input().split()))
B = []
print(*counting_sort(A,B,max(A)))