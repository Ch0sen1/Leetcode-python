class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals, key = lambda x:x[0])
        for start, end in intervals:
            if not heap:
                heapq.heappush(heap, end)
            else:
                if start < heap[0]:
                    heapq.heappush(heap, end)
                else:
                    heapq.heappush(heap, end)
                    heapq.heappop(heap)
        return len(heap)
            