class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        length = len(nums)
        
        if k > 0:
            self.swaparry(nums, 0, length - 1)
            self.swaparry(nums, 0, k - 1)
            self.swaparry(nums, k, length - 1)
        
        
    def swaparry(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
         