class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dest = -(x * x  + y * y)
            if len(heap) >= k:
                heapq.heappush(heap, (dest, x, y))
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (dest, x, y))
        
        return [[x,y]for dest,x,y in heap]