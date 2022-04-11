class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                cur = stack.pop()
                pre = stack.pop()
                if c == '*':
                    stack.append(pre * cur)
                elif c == '+':
                    stack.append(pre + cur)
                elif c == '-':
                    stack.append(pre - cur)
                elif c == '/':
                    stack.append(int(pre/cur))
        
        return stack.pop()