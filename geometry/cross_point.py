from math import sqrt
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
        return 1
    elif cross(a, b) < -EPS:
        # 'CLOCKWISE'
        return -1
    elif dot(a, b) < 0:  # ??????????????????a,b????????????????????????
        # 'ONLINE_BACK'
        return 2
    elif a.norm() < b.norm():  # a,b??????????????????????????? ?????? b???a???????????????
        # 'ONLINE_FRONT'
        return -2
    else:
        # 'ON_SEGMENT'
        return 0

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

q = int(input())
for i in range(q):
    L = list(map(int,input().split()))
    v0 = Vector([L[0],L[1]])
    v1 = Vector([L[2],L[3]])
    v2 = Vector([L[4],L[5]])
    v3 = Vector([L[6],L[7]])
    print(*cross_point(v0,v1,v2,v3))