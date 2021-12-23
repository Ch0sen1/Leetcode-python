class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        num_in_degree = [0 for i in range(numCourses)]
        out_degree = [set() for i in range(numCourses)]
        
        for attend, require in prerequisites:
            num_in_degree[attend] += 1
            out_degree[require].add(attend)
        
        queue = deque()
        res = []
        
        for i in range(len(num_in_degree)):
            if num_in_degree[i] == 0:
                queue.append(i)
                
        while queue:
            top = queue.popleft()
            res.append(top)
            
            for can_finish in out_degree[top]:
                num_in_degree[can_finish] -= 1
                if num_in_degree[can_finish] == 0:
                    queue.append(can_finish)
        
        if len(res) != numCourses:
            return False
        
        return True
                
        