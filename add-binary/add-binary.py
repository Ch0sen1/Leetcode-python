class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = ""
        carry = 0
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            res += str(carry % 2)
            carry = carry // 2
            
        
        return res[::-1]
                
        