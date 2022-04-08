class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxheap = []
        self.k = k
        
        for num in nums:
            if len(self.maxheap) < self.k:
                heapq.heappush(self.maxheap, num)
            else:
                heapq.heappushpop(self.maxheap, num)
        

    def add(self, val: int) -> int:
        if len(self.maxheap) < self.k:
            heapq.heappush(self.maxheap, val)
        else:
            heapq.heappushpop(self.maxheap, val)
            
        return self.maxheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)