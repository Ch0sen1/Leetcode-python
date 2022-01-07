class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        
        while l < r:
            mid = (l+r) // 2
            # find the value of the first index that have greater missing element than k
            if (arr[mid] - mid) - 1 < k:
                l = mid + 1
            else:
                r = mid
        
        
        return arr[l-1] + (k -((arr[l-1] - (l-1)) - 1))
        