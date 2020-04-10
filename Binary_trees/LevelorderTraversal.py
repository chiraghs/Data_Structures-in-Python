#            Level Order Traversal( Breadth-first)
#            Queues concept store each node and print out pop 

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peak(self):
        if not self.is_empty():
            return self.items[-1].value

    def size(self):  
        return len(self.items)

    def __len__(self):
        return self.size()

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversalType):
        if traversalType == 'levelorder':
            return self.level_order(tree.root)

    def level_order(self,start):
        if start is None:
           return
        queue= Queue()
        queue.enqueue(start)
        traversal=''
        while len(queue)>0:
            traversal+= str(queue.peak()) + ' - '
            node=queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)   

        return traversal    

tree=BinaryTree(1)  #root node

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(tree.print_tree('levelorder'))        