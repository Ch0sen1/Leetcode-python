class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # case 1 All capital
        
        # case 2 all lowercase
        
        # case 3 Only the first letter is captial
        
        # else return False
        cnt = 0
        first = False
        res = False
        
        for i in range(len(word)):
            if i == 0 and word[i].isupper():
                first = True
            if word[i].isupper():
                cnt += 1
        if cnt == 0:
            res = True
        elif cnt == len(word):
            res = True
        elif cnt == 1 and first == True:
            res = True
        
        
        return res
        