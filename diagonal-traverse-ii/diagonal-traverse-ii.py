class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        res = []
        for i, r in enumerate(nums):
            for j, val in enumerate(r):
                dic[i+j].append(val)
        
        for key, value in dic.items():
            for v in value[::-1]:
                res.append(v)
        return res
            
        