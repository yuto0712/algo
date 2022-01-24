n=int(input())
A=list(map(int,input().split()))
d=int(input())
Q = list(map(int,input().split()))
def solve(i,m):
    if m==0:
        return True
    if i>=n:
        return False
    res = solve(i+1,m) or solve(i+1,m-A[i])
    
    return res 

for q in Q:
    print('yes' if solve(0,q) else 'no')
   