
def reconstruction(l,r):
    if l >= r :
        return
    c = next(Pre)
    m = In.index(c)
    reconstruction(l,m)
    reconstruction(m+1,r)
    ans.append(c)
    
ans=[]
n = int(input())
Pre = iter(list(map(int,input().split())))
In = list(map(int,input().split()))
reconstruction(0,n)
print(*ans)