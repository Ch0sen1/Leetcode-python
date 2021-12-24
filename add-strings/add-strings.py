class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1, l2 = len(num1), len(num2)
        result = []
        i = carry = 0
        length = max(len(num1), len(num2))
        
        while i < length or carry:
            digit1 = (ord(num1[i]) - ord('0')) if i < l1 else 0
            digit2 = (ord(num2[i]) - ord('0')) if i < l2 else 0
            total = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10
            result.append(str(total))
            i += 1
        
        return ''.join(result[::-1])
            
        