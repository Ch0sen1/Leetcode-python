class RandomizedSet:

    def __init__(self):
        self.dic = defaultdict()
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        ## remember the index of of element we need to remove
        remove_index = self.dic[val]
        ## get the element at the last index
        last_element = self.arr[-1]
        
        ## put the last element at the remove index
        self.arr[remove_index] = last_element
        self.dic[last_element] = remove_index
        self.arr[-1] = val
        self.arr.pop()
        self.dic.pop(val)
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()