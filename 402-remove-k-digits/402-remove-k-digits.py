class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If no elements are removed, pop last elements, (increasing order)
        while(k):
            stack.pop()
            k -= 1

        # removing leading zeros
        i = 0
        while( i <len(stack) and stack[i] == "0" ):
            i += 1
            
        return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0"       
        