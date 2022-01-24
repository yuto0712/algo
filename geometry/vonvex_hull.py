from math import sqrt,cos,atan,sin,acos
class Vector:
    def __init__(self, ls):
        '''
        ls ... list
        '''
        self.vec = ls

    def __len__(self):
        return len(self.vec)

    def __getitem__(self, idx):
        return self.vec[idx]

    def __repr__(self):
        return f'Vector({self.vec})'

    def add(self, vec):
        '''
        vec ... vector class
        '''
        assert len(self) == len(vec)
        ret = [a + b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def sub(self, vec):
        '''
        vec ... vector class
        '''
        assert len(self) == len(vec)
        ret = [a - b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def mul(self, vec):
        '''
        vec ... vector class
        '''
        assert len(self) == len(vec)
        ret = [a * b for a, b in zip(self.vec, vec.vec)]
        return Vector(ret)

    def mul_const(self,r):
        ret = [a * r for a in self.vec]
        return Vector(ret)

    def norm(self):
        tmp = sum([x * x for x in self.vec])
        return tmp

    def size(self):
        return sqrt(self.norm())


def norm(vec):
    '''
    vec ... Vector class
    '''
    return vec.norm()

def dot_dot_distance(a, b):
    return sqrt(sum([(x-y)**2 for x,y in zip(a,b)]))

def cross(a, b):
    '''
    Outer product for 2d
    a,b ... Vector class
    '''
    assert len(a) == 2 and len(b) == 2
    first = a[0] * b[1]
    second = a[1] * b[0]
    return first - second

def dot(a, b):
    return sum(a.mul(b))

def projection(a, b, p):
    base = Vector(b.sub(a))
    hypo = Vector(p.sub(a))
    r = dot(hypo, base)/norm(base)
    return a.add(base.mul_const(r))

def reflection(a, b, p):
    return p.add(projection(a,b,p).sub(p).mul_const(2))

def dot_line_distance(a, b, p):
    x = projection(a,b,p)
    return dot_dot_distance(p,x)
EPS = 1e-10
def ccw(p0, p1, p2):
    a = p1.sub(p0)
    b = p2.sub(p0)
    if cross(a, b) > EPS:
        # 'COUNTER_CLOCKWISE'
        return True
    else:
        return False
    # elif cross(a, b) < -EPS:
    #     # 'CLOCKWISE'
    #     return -1
    # elif dot(a, b) < 0:  # 同一直線状でa,bが逆を向いている
    #     # 'ONLINE_BACK'
    #     return 2
    # elif a.norm() < b.norm():  # a,bが同じ方向を向いて かつ bがaよりも長い
    #     # 'ONLINE_FRONT'
    #     return -2
    # else:
    #     # 'ON_SEGMENT'
    #     return 0

def intersection(args:list):
    x0, y0, x1, y1, x2, y2, x3, y3 = args
    p0 = Vector([x0, y0])
    p1 = Vector([x1, y1])
    p2 = Vector([x2, y2])
    p3 = Vector([x3, y3])
    return ccw(p0,p1,p2)*ccw(p0,p1,p3) <= 0 and ccw(p2,p3,p0)*ccw(p2,p3,p1)<=0

def cross_point(v0,v1,v2,v3):
    base = v1.sub(v0)
    d1 = abs(cross(base,v2.sub(v0)))
    d2 = abs(cross(base,v3.sub(v0)))
    t = d1/(d1+d2)
    return v2.add(v3.sub(v2).mul_const(t))

def cross_point_circle_line(c,r,v0,v1):
    pr = projection(v0,v1,c)
    e = v1.sub(v0).mul_const(1/v1.sub(v0).size())
    base = sqrt(r**2 - pr.sub(c).size()**2)
    return list(pr.add(e.mul_const(base))),list(pr.sub(e.mul_const(base)))

def polar(a,r):
    return Vector([a*cos(r),a*sin(r)])

def cross_point_circle_line(c0,r0,c1,r1):
    d = c1.sub(c0).size()
    if d == r0+r1:
        return list(c0.add(c1.sub(c0).mul_const(r0/(r0+r1)))),list(c0.add(c1.sub(c0).mul_const(r0/(r0+r1))))
    a = acos((r0**2+d**2-r1**2)/(2*r0*d))
    t = atan(c1.sub(c0).vec[1]/c1.sub(c0).vec[0])
    return list(c0.add(polar(r0,t+a))),list(c0.add(polar(r0,t-a)))

def contain(G,p):
    is_contain = False
    for i in range(len(G)):
        a = G[i].sub(p)
        b = G[(i+1)%len(G)].sub(p)
        if abs(cross(a,b)) < EPS and dot(a,b) < EPS:
            return 1
        if a[1] > b[1]:
            a,b = b,a
        if a[1] < EPS and b[1] > EPS and cross(a,b) > EPS:
            is_contain = (not is_contain)
    return 2 if is_contain else 0

def convex_hull(points: list):
    points.sort(key=lambda x: (x[0], x[1]))
    if len(points) < 3:
        # 点が2点しかないならば線しかないが、
        # 今回は制約によりこうなる状況はないので無視する。
        pass

    # 凸包の上部(イメージはP403の図)
    conv_upper = [points[0], points[1]]  # 初期値として最初の二点が与えられます。
    for p in points[2:]:
        # 反時計回りである限りは
        while len(conv_upper) >= 2 and ccw(conv_upper[-2], conv_upper[-1], p):
            # conv_upper[-1]は凸包を作る点ではないので捨てる
            conv_upper.pop()
        conv_upper.append(p)

    # 凸包の下部
    points = points[::-1]
    conv_lower = [points[0], points[1]]
    for p in points[2::]:
        # 反時計回りである限りは
        while len(conv_lower) >= 2 and ccw(conv_lower[-2], conv_lower[-1], p):
            conv_lower.pop()
        conv_lower.append(p)

    ret = conv_upper[1:-1] + conv_lower #両端はダブっているので片方削除
    return ret[::-1]
# load data
N = int(input())
points = []
for _ in range(N):
    points.append(Vector(list(map(int, input().split()))))

ans = convex_hull(points)
print(len(ans))

idx_s = ans.index(min(ans, key=lambda x:(x[1],x[0])))
for i in range(idx_s,idx_s+len(ans)):
    idx = i%len(ans)
    p = list(ans[idx])
    print(*p)

# # 可視化用

import matplotlib.pyplot as plt
x = [x[0] for x in points]
y = [y[1] for y in points]
plt.scatter(x, y)
plt.show()