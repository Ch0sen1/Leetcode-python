class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return -1
        dic = defaultdict(list)
        for i, num in enumerate(arr):
            dic[num].append(i)
            
        visited_index = set()
        visited_group = set()
        
        q = deque()
        q.append((0,0))
        while q:
            index, step = q.popleft()
            if index == len(arr) - 1:
                return step
            # first two type of jump
            for neigh in [(index - 1), (index + 1)]:
                if 0 <= neigh < len(arr) and neigh not in visited_index:
                    q.append((neigh, step+1))
                    visited_index.add(neigh)
            
            # third type of jump
            
            if arr[index] not in visited_group:
                for neigh in dic[arr[index]]:
                    if neigh not in visited_index:
                        q.append((neigh, step+1))
                        visited_index.add(neigh)
                visited_group.add(arr[index])
            
        return -1
            
            
                
        
        