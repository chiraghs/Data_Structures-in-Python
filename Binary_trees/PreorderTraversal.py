#                              Three types of traversal
#                                   DepthFirst-search                                        &&   BreadthSearchTraversal
#             |                               |                                  |
#     in-order traversal           **pre-order traversal**                post-order traversal
#
#  left --> root --> right         root --> left --> right               left --> right --> root

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversalType):
        if traversalType == 'preorder':
            return self.preorder_print(tree.root,'')
        if traversalType == 'inorder':
            return self.inorder_print(tree.root,'')    

    def preorder_print(self,start,traversal):
        if start:
            traversal += str(start.value) + ' - '  #traversal = traversal + str(start.value
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal 

    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + ' - ')
            traversal = self.inorder_print(start.right,traversal)
        return traversal         

tree=BinaryTree(1)  #root node

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))