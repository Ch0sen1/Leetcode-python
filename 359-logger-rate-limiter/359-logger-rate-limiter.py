class Logger:

    def __init__(self):
        self.dic = defaultdict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.dic.keys():
            if timestamp < self.dic[message]:
                return False
            else:
                self.dic[message] = timestamp + 10
                return True
        else:
            self.dic[message] = timestamp + 10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)