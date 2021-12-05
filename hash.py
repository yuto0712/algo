n=int(input())
D={}
m=1046527

def to_digit(string):
    string = string.replace('A','1')
    string =string.replace('T','2')
    string =string.replace('C','3')
    string =string.replace('G','4')

    return int(string)

def h1(key):
    return key % m

def h2(key):
    return 1+(key % (m-1))

def h(key,i):
    return (h1(key) + i*h2(key)) % m

   
def insert(T,key):
    i = 0
    while True:
        j = h(key,i)
        if j not in T:
            T[j] = key
            return j
        else:
            i+=1

def search(T,key):
    i=0
    while True:
        j = h(key,i)
        if j in T:
            if T[j] == key:
                print('yes')
                break
        elif j not in T or i>=m:
            print('no')
            break
        else:
            i+=1

for _ in range(n):
    com,s=map(str,input().split())
    if com == 'insert':
        insert(D,to_digit(s))
    else:
        search(D,to_digit(s))