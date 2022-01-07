class RandomizedSet:

    def __init__(self):
        self.dic = Counter()
        self.nums = []
        
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        remove_index = self.dic[val]
        last_value = self.nums[-1]
        
        self.dic[last_value] = remove_index
        self.nums[-1], self.nums[remove_index] = self.nums[remove_index], self.nums[-1]
        self.nums.pop()
        self.dic.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()