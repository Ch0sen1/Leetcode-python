class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i , temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            while stack and temp > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                distance = i - prev_i
                res[prev_i] = distance
            stack.append((temp , i))
        
        return res
                