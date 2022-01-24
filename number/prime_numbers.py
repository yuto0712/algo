def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3,int(n**(1/2))+1,2):
        if n%i == 0:
            return False
    return True
ans=0
n = int(input())
for i in range(n):
    if isPrime(int(input())):
        ans+=1
print(ans)
