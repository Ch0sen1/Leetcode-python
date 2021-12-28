class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxHeap = [- cnt for cnt in c.values()]
        heapq.heapify(maxHeap)
        q = deque()
        
        time = 0
        
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    q.append([freq, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
                
            