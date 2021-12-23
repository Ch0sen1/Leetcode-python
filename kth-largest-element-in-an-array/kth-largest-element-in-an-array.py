class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        ## if looking for largest, use min heap,
        ## vice versa, use max heap, and put -
        for num in nums:
            if len(heap) >= k:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,num)
                
        
        return heapq.heappop(heap)
            
                
        