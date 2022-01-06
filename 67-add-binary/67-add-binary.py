class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1]
        b = b[::-1]
        res = ""
        
        length = max(len(a), len(b))
        
        i = 0
        carry = 0
        
        while i < length or carry:
            if i < len(a):
                carry += ord(a[i]) - ord('0')
            if i < len(b):
                carry += ord(b[i]) - ord('0')
                
            total = carry % 2
            res += str(total)
            carry = carry // 2
            i += 1
            
        return res[::-1]
            
        