n=int(input())
S=list(map(int,input().split()))

q=int(input())
T=list(map(int,input().split()))
ans=0
for t in T:
    left=0
    right=n
    while left < right:
        mid=(left+right)//2
        if S[mid] == t:
            ans+=1
            break
        elif S[mid] < t:
            left = mid+1
        else:
            right = mid
            
print(ans)        
        