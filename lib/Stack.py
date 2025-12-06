class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = list(items)
        self.limit = limit
        #pass

    def isEmpty(self):
        return len(self.items) == 0
        # pass

    def push(self, item):
        if not self.full():
            self.items.append(item)
        #pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        #pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        # pass
    
    def size(self):
        return len(self.items)
        # pass

    def full(self):
        return len(self.items) >= self.limit
        # pass

    def search(self, target):
        try:
            index = self.items.index(target)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
        # pass
