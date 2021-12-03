class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        

class BST():
    def __init__(self):
        self.root = None
    
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
    
    def preorder(self,u):
        if u == None:
            return
        print('',u.data,end='')
        self.preorder(u.left)
        self.preorder(u.right)
        
    def inorder(self,u):
        if u == None:
            return
        self.inorder(u.left)
        print('',u.data,end='')
        self.inorder(u.right)
        
    def postorder(self,u):
        if u == None:
            return
        self.postorder(u.left)
        self.postorder(u.right)
        print('',u.data,end='')

BST = BST()
n = int(input())
for _ in range(n):
    comnum = list(map(str,input().split()))
    if len(comnum) == 2:
        num = int(comnum[1])
        BST.insert(num)
    else:
        BST.inorder(BST.root)
        print()
        BST.preorder(BST.root)
        print()
