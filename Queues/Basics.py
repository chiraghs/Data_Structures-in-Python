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
            return self.items[-1]

    def size(self):
        return len(self.items) 

    def __len__(self):
        return self.size()

queue = Queue()
i=0
while(i<5):
 queue.enqueue(i)
 print(queue.items)
 i+=1

print(queue.items)
print(queue.peak())

while(len(queue)>0):
    queue.dequeue()
    print(queue.items)

queue.enqueue(100)
print(queue.items)                 