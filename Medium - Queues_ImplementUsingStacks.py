class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if self.first[0]:
            return self.first[0]
        else:
            return None
        
        
    def pop(self):
        if self.first[0]:
            return self.first.pop(0)
        else:
            return None
        
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()