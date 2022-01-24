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
n = int(readline())
for _ in range(n):
    comnum = list(map(str,readline().split()))
    if comnum[0] == 'insert':
        num = int(comnum[1])
        BST.insert(num)
    elif comnum[0] == 'find':
        print(BST.find(int(comnum[1]), BST.root))
    else:
        BST.inorder(BST.root)
        print()
        BST.preorder(BST.root)
        print()
