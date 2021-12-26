class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        givenNumber = [2, 3, 5]
        
        for num in givenNumber:
            
            while n % num == 0:
                n = n // num
                
        return n == 1
        