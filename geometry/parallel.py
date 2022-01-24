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

EPS = 1e-10

n = int(input())
for i in range(n):
    p0x,p0y,p1x,p1y,p2x,p2y,p3x,p3y = map(int, input().split())
    v1 = Vector([p1x-p0x,p1y-p0y])
    v2 = Vector([p3x-p2x,p3y-p2y])
    if dot(v1, v2) == 0:
        print(1)
    elif cross(v1, v2) == 0:
        print(2)
    else:
        print(0)
