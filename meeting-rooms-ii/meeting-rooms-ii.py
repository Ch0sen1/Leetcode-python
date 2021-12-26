class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        heap = []
        for i in range (len(intervals)):
            if heap and intervals[i][0] >= heap[0]:
                # heapq.heappop(heap)
                heapq.heapreplace(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        return len(heap)
                
            
            
                
            
        