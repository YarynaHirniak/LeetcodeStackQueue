class Stack:
    def __init__(self):
        self.stack = []

    def put(self, x):
        self.stack.append(x)

    def get(self):
        if self.empty():
            return None
        return self.stack.pop()
    
    def empty(self):
        return len(self.stack) == 0
    
    def qsize(self):
        return len(self.stack)
class MyQueue(object):

    def __init__(self):
        self.queue = Stack()
        self.queue2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.put(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(self.queue.qsize()):
            first = self.queue.get()
            self.queue2.put(first)
        self.queue2.get()
        for i in range(self.queue2.qsize()):
            self.queue.put(self.queue2.get())
        return first
            
        

    def peek(self):
        """
        :rtype: int
        """
        for i in range(self.queue.qsize()):
            first = self.queue.get()
            self.queue2.put(first)

        for i in range(self.queue2.qsize()):
            self.queue.put(self.queue2.get())
        return first
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.empty()
