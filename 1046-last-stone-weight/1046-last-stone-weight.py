
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)
        while len(q) > 1:
            diff = (-heapq.heappop(q) - -heapq.heappop(q))
            heapq.heappush(q, -diff)
        
        return -q[0]
        
        
        