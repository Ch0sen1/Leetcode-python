"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = defaultdict(Node)
        old_to_new[node] = Node(node.val)
        self.dfs(node, old_to_new)
        return old_to_new[node]
        
    
    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])
            
            
        
        
        
        