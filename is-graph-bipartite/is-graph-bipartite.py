class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = defaultdict()
        for i in range(len(graph)):
            if i not in seen:
                if self.dfs(graph, i, 1, seen) == False:
                    return False
        return True
                           
        
        
    def dfs(self, graph, i, color, seen):
        if i in seen:
            if seen[i] != color:
                return False
            return True
        seen[i] = color
        neighs = graph[i]
        for neigh in neighs:
            if self.dfs(graph, neigh, -color, seen) == False:
                return False
        return True
        
            
        
        
        