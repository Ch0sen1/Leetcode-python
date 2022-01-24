class Logger:

    def __init__(self):
        self.win = deque()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.win and timestamp - self.win[0][0] >= 10:
            self.win.popleft()
        
        if any(message in msg for t, msg in self.win):
            return False
        
        self.win.append([timestamp, message])
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)