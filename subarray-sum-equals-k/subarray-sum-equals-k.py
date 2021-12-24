class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = Counter()
        c[0] = 1
        total = 0
        count = 0
        for num in nums:
            total += num
            count += c[total -k]
            c[total] += 1
        return count
            
        
        