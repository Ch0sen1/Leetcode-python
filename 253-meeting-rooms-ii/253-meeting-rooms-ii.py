class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals, key = lambda f:f[0])
        for start, end in intervals:
            if not heap:
                heap.append(end)
            else:
                if start >= heap[0]:
                    heapq.heappush(heap, end)
                    heapq.heappop(heap)
                else:
                    heapq.heappush(heap, end)
            
            
        return len(heap)
            