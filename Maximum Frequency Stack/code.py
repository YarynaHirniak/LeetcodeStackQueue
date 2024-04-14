from collections import defaultdict, deque

class FreqStack(object):

    def __init__(self):
        self.freq = defaultdict(int) 
        self.group = defaultdict(deque)
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1  
        freq = self.freq[val]
        self.group[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self):
        """
        :rtype: int
        """
        if self.max_freq == 0:
            return None 
        val = self.group[self.max_freq].pop() 
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val


