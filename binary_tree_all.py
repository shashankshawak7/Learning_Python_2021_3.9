#binary tree

class Node:
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        self.data = data

    def CreateTree(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.CreateTree(data)
            else:
                if self.right  is None:
                    self.right = Node(data)
                else:
                    self.right.CreateTree(data)
        else:
            self.data = data
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()
    # binary tree traversal

    # inorder traversal
    def inordertraversal( self, root):
        res = []
        if root:
            res = res + self.inordertraversal(root.left)
            res.append(root.data)
            res = res + self.inordertraversal(root.right)   
        return res
    # pre order traversal
    def preordertraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preordertraversal(root.left)
            res = res + self.preordertraversal(root.right)
        return res
    def postordertraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preordertraversal(root.right)
            res = res + self.preordertraversal(root.left)
        return res

    # print only left view binary tree

def leftView(root, level, dict):
        # base case
    if root is None:
        return
       # insert the current node and level information into the map
    dict[level] = root.data
    
       # recur for the right subtree before the left subtree
    leftView(root.right, level + 1, dict)
    leftView(root.left, level + 1, dict)
    return dict

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)




def main():
    #creating tree
    root = Node(10)
    root.CreateTree(5)
    root.CreateTree(15)
    # root.CreateTree(1)
    # root.CreateTree(10)
    # root.CreateTree(9)
    # root.CreateTree(200)
    #printTree
    printTree(root)
    print(root.inordertraversal(root))
    #print(root.preordertraversal(root))
    #print(root.postordertraversal(root))
    #print(leftView(root,1,{}))
    
if __name__=='__main__':
    main()


