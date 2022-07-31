class Solution:
    def wordSubsets(self, words1, words2):
        res = []
        need = Counter()
        res = set(words1)
        
        for w in words2:
            for c in w:
                num = w.count(c)
                if c not in need or num > need[c]:
                    need[c] = num
        
        for w in words1:
            for letter in need:
                if need[letter] > w.count(letter):
                    res.remove(w)
                    break
        
        return list(res)
            
            
        