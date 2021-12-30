class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        stack.append(["!",0])
        res = ""
        
        for c in s:
            if c != stack[-1][0]:
                stack.append([c,1])
            else:
                stack[-1][1] = stack[-1][1] + 1
                if stack[-1][1] == k:
                    stack.pop()
        
        for key, value in stack:
            res += key * value
        
        return res
        
        