class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        expectWord = defaultdict(list)
        res = 0
        
        for word in words:
            expectWord[word[0]].append(word)
        
        for c in s:
            nextExpectWord = expectWord[c]
            expectWord[c] = []
            for word in nextExpectWord:
                if len(word) == 1:
                    res += 1
                else:
                    expectWord[word[1]].append(word[1:])
        
        return res
            
                
                