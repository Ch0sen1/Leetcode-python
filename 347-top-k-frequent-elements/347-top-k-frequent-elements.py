class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        order = [set() for i in range(len(nums)+1)]
        c = Counter(nums)
        res = []
        for key, value in c.items():
            order[value].add(key)
            
        for i in range(len(order)-1, -1, -1):
            if order[i]:
                for ele in order[i]:
                    res.append(ele)
                    k -= 1
                    if k == 0:
                        return res
        
        return res
        
            
        