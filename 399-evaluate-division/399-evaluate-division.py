class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = defaultdict(list)
        def buildGraph(equations, values):
            def addNode(s, e, v):
                if not G[s]:
                    G[s] = [(e, v)]
                else:
                    G[s].append((e,v))
            
            for node, value in zip(equations, values):
                start,end = node
                addNode(start, end, value)
                addNode(end, start, 1/value)
                
        
        
        def getQuery(query):
            s, e = query
            
            if not G[s] or not G[e]:
                return -1.0
            
            q = deque()
            q.append((s,1.0))
            visited = set()
            
            while q:
                node, curProduct = q.popleft()
                if node == e:
                    return curProduct
                visited.add(node)
                for neigh, val in G[node]:
                    if neigh not in visited:
                        q.append((neigh, curProduct * val))
            return -1.0
            
        buildGraph(equations, values)
        return [getQuery(q) for q in queries ]
                
                
            
            
            
            
                    
                    
                
        