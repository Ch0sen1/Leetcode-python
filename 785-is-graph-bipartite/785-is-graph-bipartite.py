class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # i is itself, List[i] is its neighbors
        dic = defaultdict()
        for i in range(len(graph)):
            if i not in dic:
                if self.bfs(graph, i, dic) == False:
                    return False
        return True
        
        
    def bfs(self, graph, i, dic):
        q = deque()
        q.append((i,1))
        while q:
            node, color = q.popleft()
            if node in dic:
                if dic[node] != color:
                    return False
            else:
                dic[node] = color
                for neigh in graph[node]:
                    q.append((neigh, -color))
        return True
                
                
        
        
            
        
        
        