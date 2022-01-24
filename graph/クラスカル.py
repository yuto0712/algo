from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] < self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self,x):
        return -self.parents[self.find(x)]

    def same(self,x, y):
        return self.find(x) == self.find(y)

    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i,x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)

        return group_members

    def __str__(self) -> str:
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def kruskal(n,Edges):
    uf = UnionFind(n)
    edges = sorted(Edges)
    num_nodes = 0
    ret = 0
    for w,s,t in edges:
        if num_nodes == n-1:
            break
        if uf.same(s,t):
            continue
        uf.union(s,t)
        ret += w
        num_nodes += 1
    return ret

V,E = map(int,input().split())
edge_list = []
for _ in range(E):
    s,t,w = map(int,input().split())
    edge_list.append((w,s,t)) #辺を軽い順にソートするので、w,s,tの順番

print(kruskal(V,edge_list))

# Atcoder用--------------------------------------------------------

# from scipy.sparse import lil_matrix
# from scipy.sparse.csgraph import minimum_spanning_tree  # この関数の引数は隣接行列

# # load data
# n_V, n_E = list(map(int, input().split()))
# adjmat = lil_matrix((n_V, n_V))
# for _ in range(n_E):
#     s, t, w = list(map(int, input().split()))
#     adjmat[s, t] = w
#     adjmat[t, s] = w

# mst = minimum_spanning_tree(adjmat)
# print(int(mst.sum()))