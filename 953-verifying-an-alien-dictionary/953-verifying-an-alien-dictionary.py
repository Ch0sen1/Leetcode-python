class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderdict = Counter()
        new_word = []
        for i, o in enumerate(order):
            orderdict[o] = i
            
        for w in words:
            new = []
            for i in range(len(w)):
                new.append(orderdict[w[i]])
            new_word.append(new)
            
        for w1, w2 in zip(new_word, new_word[1:]):
            if w1 > w2:
                return False
        return True
            
            
        