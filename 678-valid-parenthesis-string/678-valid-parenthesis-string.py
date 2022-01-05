class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        para_stack = []
        for i, c in enumerate(s):
            if c == '(':
                para_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            elif c == ')':
                if para_stack:
                    para_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while para_stack and star_stack:
            if star_stack[-1] > para_stack[-1]:
                star_stack.pop()
                para_stack.pop()
            else:
                break
        
        return len(para_stack) == 0
            
        