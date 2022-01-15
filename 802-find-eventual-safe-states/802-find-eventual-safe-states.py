class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        out_degree = defaultdict()
        in_degree = defaultdict(list)
        q = deque()
        res = []
        
        for i in range(len(graph)):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                q.append(i)
            for neigh in graph[i]:
                in_degree[neigh].append(i)
        
        
        while q:
            node = q.popleft()
            
            for neigh in in_degree[node]:
                out_degree[neigh] -= 1
                if out_degree[neigh] == 0:
                    q.append(neigh)
                    
                    
        for i in range(len(graph)):
            if out_degree[i] == 0:
                res.append(i)
            
        return res
                
            