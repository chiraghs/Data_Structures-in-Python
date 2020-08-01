class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    def postordertraversal(self,start,traversal):
        if start:
            traversal = self.postordertraversal(start.left,traversal)
            traversal = self.postordertraversal(start.right,traversal)
            traversal += str(start.value) + '-'
        return traversal    

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.postordertraversal(tree.root,''))