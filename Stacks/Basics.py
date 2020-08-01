class Staack:  #Last in first Out
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

stack = Staack()
i=0
while(i<5):
 stack.push(i)
 print(stack.items)
 i+=1

print(stack.items)
print(stack.peak())

while(len(stack)>0):
    stack.pop()
    print(stack.items)

stack.push(100)
print(stack.items)
print(stack.pop())