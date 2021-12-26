class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        res = []
        bucket = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            c[n] += 1 
        for number, count in c.items():
            bucket[count].append(number)
            
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for a in bucket[i]:
                    res.append(a)
                    if len(res) == k:
                        return res
                
            
        