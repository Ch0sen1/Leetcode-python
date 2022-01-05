class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        array = list(s)
        for i, c in enumerate(array):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    array[i] = ""
        
        while stack:
            array[stack.pop()] = ""
            
        return "".join(array)
            
                
        
                
            