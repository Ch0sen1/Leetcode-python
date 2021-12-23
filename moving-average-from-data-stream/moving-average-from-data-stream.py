class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.length = 0
        
        

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.sum += val
        else:
            oldval = self.queue.popleft()
            self.queue.append(val)
            self.sum -= oldval
            self.sum += val
            
        return self.sum / len(self.queue)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)