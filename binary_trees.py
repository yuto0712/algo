class BinaryTreeNode:
    def __init__(self):
        self.parent = -1
        self.sibling = -1
        self.degree = 0

        
def cal_depth(node_id,d=0):
    Tree[node_id].depth = d
    if Tree[node_id].left != -1:
        cal_depth(Tree[node_id].left,d+1)
        Tree[node_id].type = 'internal node'
    if Tree[node_id].right != -1:
        cal_depth(Tree[node_id].right,d+1)
        Tree[node_id].type = 'internal node'
    if Tree[node_id].right == -1 and Tree[node_id].left == -1:
        Tree[node_id].type = 'leaf'
        
def cal_height(node_id,d=0):
    h1,h0 = 0,0
    if Tree[node_id].left != -1:
        h0 = cal_height(Tree[node_id].left) + 1
    if Tree[node_id].right != -1:
        h1 = cal_height(Tree[node_id].right) + 1
    Tree[node_id].height = max(h0,h1)
    return max(h0,h1)


n=int(input())
Tree = [BinaryTreeNode() for i in range(n)]

for _ in range(n):
    tree_info = list(map(int,input().split()))
    node_id = tree_info[0]
    Tree[node_id].left = tree_info[1]
    Tree[node_id].right = tree_info[2]
    
    if Tree[node_id].left != -1:
        Tree[Tree[node_id].left].parent = node_id
        Tree[node_id].degree += 1
    if Tree[node_id].right != -1:
        Tree[Tree[node_id].right].parent = node_id
        Tree[node_id].degree += 1
    if Tree[node_id].right != -1 and Tree[node_id].left != -1:
        Tree[Tree[node_id].right].sibling = Tree[node_id].left
        Tree[Tree[node_id].left].sibling = Tree[node_id].right


root_id = [i for i,t in enumerate(Tree) if t.parent == -1][0]
cal_depth(root_id)
cal_height(root_id)
Tree[root_id].type = 'root'

for i,t in enumerate(Tree):
    print(f'node {i}: parent = {t.parent}, sibling = {t.sibling}, degree = {t.degree}, depth = {t.depth}, height = {t.height}, {t.type}')