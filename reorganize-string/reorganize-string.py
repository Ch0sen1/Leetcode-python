class Solution:
    def reorganizeString(self, s: str) -> str:
        # heap to store the most frequent element,
        # we want to use the most frequent element first
        maxHeap = []
        heapq.heapify(maxHeap)
        c = Counter(s)
        prev = None
        res = ""
        # push the element to the heap
        for key, value in c.items():
            heapq.heappush(maxHeap, [-value, key])
        
        # loop throug the Heap, if there is still have element on heap
        # or there is still a hold for a element continue the loop
        while maxHeap or prev:
            # if there is no extra element in the heap, but there is still a hold for a "a", since we cant repeat
            # return an empty
            if prev and not maxHeap:
                return ""
            # pop the freq, and char in the heap
            freq, char = heapq.heappop(maxHeap)
            res += char
            # used element one time
            freq += 1
            
            # we can push the hold back to heap, since we already aovid adjcent
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            # if there still have count for the element, make it to a hold, avoid adj
            if freq != 0:
                prev = [freq, char]
            
        return res
            
            
            
        
            
        
        