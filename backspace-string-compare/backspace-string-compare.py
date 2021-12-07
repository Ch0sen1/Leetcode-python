class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i, c in enumerate(s):
            if c == '#' and stack1:
                stack1.pop()
            elif c != '#':
                stack1.append(c)
        
        for i, c in enumerate(t):
            if c == '#' and stack2:
                stack2.pop()
            elif c != '#':
                stack2.append(c)
                
        return stack1 == stack2
            