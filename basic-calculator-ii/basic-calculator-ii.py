class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
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
                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                sign = c
                num = 0
        return sum(stack)
                
                    
                
        