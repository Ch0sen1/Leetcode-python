class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        for index in range(len(nums)-1, -1, -1):
            if (nums[i] * nums[i]) > (nums[j] * nums[j]):
                res[index] = nums[i] * nums[i]
                i += 1
            else:
                res[index] = nums[j] * nums[j]
                j -= 1
        return res
                
        