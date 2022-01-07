class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        num = 0
        s += '$'
        stack = []
        for i in range(len(s)):
            c = s[i]
            
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev/num))
                sign = c
                num = 0
        return sum(stack)
                    
                    
                
        