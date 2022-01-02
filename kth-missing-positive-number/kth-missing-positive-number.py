class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        
        while l < r:
            mid = (l+r) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid
        
        return l + k
        