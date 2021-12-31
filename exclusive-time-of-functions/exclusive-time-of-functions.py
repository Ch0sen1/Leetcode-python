class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        
        for log in logs:
            logId, logType, logTime = log.split(":")
            logId = int(logId)
            logTime = int(logTime)
            
            if logType == 'start':
                if stack:
                    res[stack[-1][0]] += logTime - stack[-1][1] - 1
                stack.append([logId, logTime])
                
            elif logType == 'end':
                prev = stack.pop()
                timeSpend = logTime - prev[1] + 1
                res[logId] += timeSpend
                if stack:
                    stack[-1][1] = logTime               
        
        return res
                
            
        