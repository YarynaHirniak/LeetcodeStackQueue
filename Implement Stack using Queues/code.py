class Queue:
    def __init__(self):
        self.queue = []

    def put(self, x):
        self.queue.append(x)

    def get(self):
        if self.empty():
            return None
        return self.queue.pop(0)

    def qsize(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

class MyStack(object):

    def __init__(self):
        self.stack = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.put(x)
        for i in range(self.stack.qsize()-1):
            self.stack.put(self.stack.get())

        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.get()

    def top(self):
        """
        :rtype: int
        """
        top_el = self.stack.get()
        self.stack.put(top_el)
        for i in range(self.stack.qsize()-1):
            self.stack.put(self.stack.get())
        return top_el
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.empty()
