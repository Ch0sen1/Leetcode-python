class Solution:
    def isValid(self, s: str) -> bool:
        dic = defaultdict()
        
        dic[')'] = '('
        dic['}'] = '{'
        dic[']'] = '['
        
        stack = []
        
        for c in s:
            if c in ['(', '{','[']:
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        