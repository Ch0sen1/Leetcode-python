class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        r = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    r += 1
                
        return len(stack) + r