class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ans = 0
        
        for num in nums:
            need = k - num
            if dic[need] > 0:
                ans += 1
                dic[need] -= 1
            else:
                dic[num] += 1
        
        return ans
        