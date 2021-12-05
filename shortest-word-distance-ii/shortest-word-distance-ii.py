class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dic = collections.defaultdict(list)
        self.l = len(wordsDict)
        for i, x in enumerate(wordsDict):
            self.dic[x].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.dic[word1], self.dic[word2]
        res = self.l
        i = j = 0
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)