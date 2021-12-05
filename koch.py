def koch(d,p1,p2):
    if d==0:
        return
    t = p1/3 + p2*2/3
    s = p1*2/3 + p2/3
    u = (p1+p2)/2 + 3**(1/2)*np.rot90((t-s).reshape(1, 2)).reshape(2,)/2

    koch(d-1,p1,s)
    print(*s)
    koch(d-1,s,u)
    print(*u)
    koch(d-1,u,t)
    print(*t)
    koch(d-1,t,p2)
    
    # print(f's{s},t{t},u{u}')
n=int(input())
import numpy as np
print(0,0)
koch(n,np.array([0,0]),np.array([100,0]))
print(100,0)