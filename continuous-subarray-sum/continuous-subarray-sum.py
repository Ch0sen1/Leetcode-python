class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        c = Counter()
        c[0] = -1
        for i , num in enumerate(nums):
            if k != 0:
                total = (total + num) % k
            else:
                total += num
            if total not in c:
                c[total] = i
            else:
                if i - c[total] >= 2:
                    return True
        return False
        