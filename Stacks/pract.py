class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.pop()  

    def top(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def __len__(self):
        return size(self.items)

staack = stack()
i = 0
while(i < 5):
    staack.push(i)
    print(staack.items)
    i+=1                    