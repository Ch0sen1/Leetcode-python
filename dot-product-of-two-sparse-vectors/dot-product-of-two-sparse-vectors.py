class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = defaultdict()
        for i, num in enumerate(nums):
            if num != 0:
                self.dic[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for key, val in self.dic.items():
            if key in vec.dic:
                total += (val * vec.dic[key])
        return total
        
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)