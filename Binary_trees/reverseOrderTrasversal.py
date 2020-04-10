#            Level Order Traversal( Breadth-first)
#            Queues,stack concept ( store each node and push to stack and print out from stack 

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

class Staack:  #Last in Last Out
    def __init__(self): #Initialize constructor
        self.items=[]

    def push(self,item):  #first in last out push/append element
        self.items.append(item)    

    def pop(self):
        if not self.is_empty():
           return self.items.pop()

    def is_empty(self):
        return len(self.items)==0

    def peak(self):
        if not self.is_empty():
            return self.items[-1]

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
        if traversalType == 'reverseorder':
            return self.reverse_order(tree.root)

    def reverse_order(self,start):
        if start is None:
           return
        queue= Queue()
        stack= Staack()
        queue.enqueue(start)
        traversal=''
        while len(queue)>0:
            node=queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right) 
            if node.left:
                queue.enqueue(node.left)
              

        while len(stack)>0 :
            traversal += str(stack.pop().value) + ' - ' 
        return traversal    

tree=BinaryTree(1)  #root node

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print(tree.print_tree('reverseorder'))        