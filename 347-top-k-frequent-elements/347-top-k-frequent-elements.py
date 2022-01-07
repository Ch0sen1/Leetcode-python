class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        order = [[] for i in range(len(nums)+1)]
        res = []
        
        for key, value in c.items():
            order[value].append(key)
            
        for i in range(len(order)-1, -1, -1):
            if order[i]:
                for element in order[i]:
                    res.append(element)
                    k -= 1
                    if k == 0:
                        return res
                
                
                
            
        