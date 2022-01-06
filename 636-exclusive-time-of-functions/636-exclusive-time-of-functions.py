class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        
        for i in range(len(logs)):
            log = logs[i].split(':')
            log_id, log_type, log_time = log
            log_id, log_time = int(log_id) , int(log_time)
            
            if log_type == 'start':
                
                if stack:
                    res[stack[-1][0]] += log_time - stack[-1][1]
                stack.append([log_id, log_time])
                
                
            elif log_type == 'end':
                prev_id, prev_time = stack.pop()
                time_spend = log_time - prev_time + 1
                res[log_id] += time_spend
                if stack:
                    stack[-1][1] = log_time + 1
        return res
                
                