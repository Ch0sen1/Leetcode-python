class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)
        

    def pick(self, target: int) -> int:
        if target in self.dic:
            curList = self.dic[target]
            index = randrange(0, len(curList))
            return curList[index]
            
            
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)