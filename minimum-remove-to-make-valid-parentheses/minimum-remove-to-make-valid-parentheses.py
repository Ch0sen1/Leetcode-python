class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        array = list(s)
        stack = []
        for i, c in enumerate(array):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    array[i] = ''
            
        while stack:
            index = stack.pop()
            array[index] = ''
        
        return ''.join(array)
                
        
                
            