class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            temp = 0
            for i in range(len(num)):
                temp += int(num[i])
            num = str(temp)
        
        return int(num)
                
            
        