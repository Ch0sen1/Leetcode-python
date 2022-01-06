class Solution:
    def simplifyPath(self, path: str) -> str:
        part = path.split("/")
        stack = []
        for c in part:
            if c == '.' or c =='':
                continue
            elif c =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
                
        return '/' + '/'.join(stack)
        