class TreeNode:
    def __init__(self):
        self.parent = -1
        self.children = []
        
def cal_depth(node_id,d=0):
    Tree[node_id].depth = d
    for child in Tree[node_id].children:
        cal_depth(child,d+1)
n=int(input())
Tree = [TreeNode() for i in range(n)]

for _ in range(n):
    tree_info = list(map(int,input().split()))
    node_id = tree_info[0]
    k = tree_info[1]
    if k > 0:
        children = tree_info[2:]
        Tree[node_id].children = children
        Tree[node_id].type = 'internal node'
    else:
        Tree[node_id].type = 'leaf'
    for child in Tree[node_id].children:
        Tree[child].parent = node_id
root_id =[i for i,t in enumerate(Tree) if t.parent == -1][0]
Tree[root_id].type = "root"
cal_depth(root_id)

for i,t in enumerate(Tree):
    print("node {}: parent = {}, depth = {}, {}, {}".format(i, t.parent, t.depth, t.type, t.children))