class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def height(self,node):
        if node is None:
            return -1
        leftHeight  = self.height(node.left)   
        rightHeight = self.height(node.right) 

        return 1 + max(leftHeight,rightHeight)

    

tree=BinaryTree(1)  #root node

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(tree.height(1))