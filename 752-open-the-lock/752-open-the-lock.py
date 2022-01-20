class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1 
        q = deque()
        q.append(['0000', 0])
        visited = set(deadends)
        
        
        def getChild(node):
            res = []
            for i in range(4):
                digit = str((int(node[i]) + 1) % 10)
                res.append(node[:i] + digit + node[i+1:])
                digit = str((int(node[i]) - 1 + 10) % 10)
                res.append(node[:i] + digit + node[i+1:])
            return res
        
        while q:
            node, step = q.popleft()
            if node == target:
                return step
            for child in getChild(node):
                if child not in visited:
                    q.append((child, step+1))
                    visited.add(child)
        
        return -1
            
        
        
        