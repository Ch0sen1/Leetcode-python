class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hold = None
        freq = 0
        res = ""
        
        
        heap = []
        if c:
            heap.append([-c,'c'])
        if b:
            heap.append([-b,'b'])
        if a:
            heap.append([-a,'a'])
        heapq.heapify(heap)
        
        while heap:
            
            # pop the most freq element in the list
            cnt, elem = heapq.heappop(heap)
            
            # if the element exist 3 times, put it into a hold or prioty q
            if res and elem == res[-1]:
                freq += 1
                if freq >= 2:
                    hold = [cnt, elem]
                    continue
            else:
                freq = 0
            
            # after adding the element not in the hold, push it back to the heap
            res += elem
            
            # push the elem with the new cnt into the heap
            cnt += 1
            if hold:
                heapq.heappush(heap,hold)
                hold = None
                
            if cnt != 0:   
                heapq.heappush(heap, [cnt, elem])
            
         
        return res
        