class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        
        while i < len(abbr) and j < len(word):
            if abbr[i] == word[j]:
                i += 1
                j += 1
            elif abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                tmp = 0
                while i < len(abbr) and abbr[i].isdigit():
                    tmp = tmp * 10 + int(abbr[i])
                    i +=1
                j += tmp
            else:
                return False
        
        return i == len(abbr) and j == len(word)
            
                
                
                    
                
            
                            
                
        
            
            
        