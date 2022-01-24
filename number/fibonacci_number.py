def fibonacci(n,F):
    if n == 0 or n == 1:
        return F[n]

    if len(F) > n:
        return F[n]
    return fibonacci(n - 1,F) + fibonacci(n-2,F)

def make_fibonacci(F):
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
n = int(input())
F = [1,1]
make_fibonacci(F)
print(F[n])