class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

tree=BinaryTree(1)  #root node

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(tree.root.value)
print(tree.value)