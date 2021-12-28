class Item(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word  
        return self.freq < other.freq
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        heap = []
        res = []
        
        for key, value in c.items():
            element = Item(key, value)
            if len(heap) >= k:
                heappush(heap, element)
                heappop(heap)
            else:
                heappush(heap, element)
        # return heap[0]
        while heap:
            res.append(heappop(heap).word)
        
        return res[::-1]
        
        