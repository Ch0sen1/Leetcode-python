class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        size = len(arr) // 2
        res = 0
        
        arr = sorted(c.values(), reverse = True)
        
        for value in arr:
            res += 1
            size -= value
            if size <= 0:
                return res
        return -1
        