class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderdict = defaultdict()
        for i, c in enumerate(order):
            orderdict[c] = i
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            for j in range(len(w1)):
                ## if the w1'j reach to the end of w2, it means w1 is longer than w2 
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if orderdict[w2[j]] < orderdict[w1[j]]:
                        return False
                    break
        
        return True
        