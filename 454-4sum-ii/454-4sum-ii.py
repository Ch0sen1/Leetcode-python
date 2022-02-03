class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = Counter()
        res = 0
        
        for a in nums1:
            for b in nums2:
                dic[a+b] += 1
                
        
        for a in nums3:
            for b in nums4:
                if -(a+b) in dic:
                    res += dic[-(a+b)]
        
        return res
                
            
        