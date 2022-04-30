class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color_dic = defaultdict()
        for i in range(len(graph)):
            if i not in color_dic:
                if self.BFS(i, graph, color_dic) == False:
                    return False
        return True
        
        
    
    def BFS(self, s, graph, color_dic):
        q = deque()
        q.append((s, 1))

        while q:
            node, color = q.popleft()
            
            if node not in color_dic:
                color_dic[node] = color
            else:
                if color_dic[node] != color:
                    return False
            
            for neigh in graph[node]:
                if neigh not in color_dic:
                    q.append((neigh, -color))
        
        return True