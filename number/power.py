MOD = 10**9+7
def pow(x,n):
    if n==0:
        return 1
    if n%2==0:
        res = pow(x*x%MOD,n//2)%MOD
    else:
        res = pow(x*x%MOD,(n-1)//2)*x%MOD
    return res

a,b = map(int,input().split())
print(pow(a,b))