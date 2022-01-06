class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        c = Counter(tasks)
        q = deque()
        res = ""
        
        # pop the most frequent element first, and add a time interval
        for key, value in c.items():
            # need to do the max number first
            heapq.heappush(heap, [-value, key])
            
        while heap or q:
            time += 1
            
            if heap:
                cur_val, cur_key = heapq.heappop(heap)
                cur_val += 1
            
            if cur_val != 0:
                q.append([cur_val, cur_key, time+n])
                cur_val, cur_key = 0, None
            
            if q:
                if q[0][2] <= time:
                    insert_val, insert_key, exit_time = q.popleft()
                    heapq.heappush(heap, [insert_val, insert_key])
        
        return time
        
        
                
            