class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        c = Counter()
        res = 0
        f = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            code = ""
            for w in word:
                code += f[(ord(w)-97)]
            
            c[code] += 1
        
        return len(c.values())
                
        
        