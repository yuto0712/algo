import sys
readline = sys.stdin.readline
class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


class BST():
    def __init__(self):
        self.root = None
        self.Pre = []
        self.Post = []
        self.In = []
    
    def insert(self,data):
        y = None
        x = self.root
        while x != None:
            y = x
            if data < x.data:
                x = x.left
            else:
                x = x.right

        if y == None:
            self.root = Node(data)
        elif data < y.data:
            y.left = Node(data)
        else:
            y.right = Node(data)

    def find(self,data,u):
        while u != None and u.data != data:
            if data < u.data:
                u = u.left
            else:
                u = u.right
        if u == None:
            return 'no'
        if u.data == data:
            return 'yes'
    
    def delete(self,data):
        u = self.root
        if u == None:
            return None
        while u.data != data:
            if data < u.data:
                u = u.left
            else:
                u = u.right
        
        if u.left == None or u.right == None:
            y = u
        else:
            y = self.get_successor(u)
        
        y.parent = self.get_parent(y)
        
        if y.left != None:
            x = y.left
        else:
            x = y.right
        
        if x != None:
            x.parent = y.parent
        
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        elif y == y.parent.right:
            y.parent.right = x
        
        if y != u:
            u.data = y.data
    

    def get_successor(self,x):
        if x.right != None:
            return self.get_minimum(x.right)
        y = self.get_parent(x)
        while y != None and x == y.right:
            x = y
            y = self.get_parent(y)
        return y
    
    def get_minimum(self,x):
        while x.left != None:
            x = x.left
        return x
    
    def get_parent(self,y):
        u = self.root
        parent = None
        while u.data != y.data:
            parent = u
            if y.data < u.data:
                u = u.left
            else:
                u = u.right
        return parent
    
    def preorder(self,u):
        if u == None:
            return
        # print('',u.data,end='')
        self.Pre.append(u.data)
        self.preorder(u.left)
        self.preorder(u.right)

    def inorder(self,u):
        if u == None:
            return
        self.inorder(u.left)
        # print('',u.data,end='')
        self.In.append(u.data)
        self.inorder(u.right)

    def postorder(self,u):
        if u == None:
            return
        self.postorder(u.left)
        self.postorder(u.right)
        self.Post.append(u.data)
        # print('',u.data,end='')

BST = BST()
n = int(readline())
for _ in range(n):
    comnum = list(map(str,readline().split()))
    if comnum[0] == 'insert':
        num = int(comnum[1])
        BST.insert(num)
    elif comnum[0] == 'find':
        ans = BST.find(int(comnum[1]), BST.root)
        print(ans)
    elif comnum[0] == 'delete':
        BST.delete(int(comnum[1]))
    else:
        BST.In = []
        BST.Pre = []
        BST.inorder(BST.root)
        BST.preorder(BST.root)
        print('',*BST.In)
        print('',*BST.Pre)