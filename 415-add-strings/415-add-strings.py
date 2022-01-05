class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ""
        
        i = j = 0
        
        carry = 0
        
        while i < len(num1) or j < len(num2) or carry:
            if i < len(num1):
                carry += int(num1[i])
                i += 1
            if j < len(num2):
                carry += int(num2[j])
                j += 1
            tmp = carry % 10
            res += (str(tmp))
            carry = carry // 10
        
        return res[::-1]
            
            
            
        