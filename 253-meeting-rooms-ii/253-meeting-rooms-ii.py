class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key = lambda i:i[0])
        for start, end in intervals:
            if not heap:
                heapq.heappush(heap, end)
            else:
                if start < heap[0]:
                    heapq.heappush(heap, end)
                else:
                    heapq.heappushpop(heap, end)
        
        return len(heap)
                    
            