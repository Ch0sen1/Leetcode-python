class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]
        
        num_in_degree = [0 for _ in range(numCourses)]
        out_degree = [set() for _ in range(numCourses)]
        
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
            return []
        
        return res