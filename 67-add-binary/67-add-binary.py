class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = a[::-1]
        b = b[::-1]
        res = []
        
        i = 0
        j = 0
        carry = 0
        while i < len(a) or j < len(b) or carry:
            if i < len(a):
                carry += int(a[i])
                i +=1
                
            if j < len(b):
                carry += int(b[j])
                j +=1
            
            total = carry % 2
            res.append(str(total))
            carry = carry // 2
        
        return ''.join(res[::-1])
        
        