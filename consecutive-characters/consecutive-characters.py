class Solution:
    def maxPower(self, s: str) -> int:
        prev_char = ""
        maxCount = 1
        count = 1
        for char in s:
            if char == prev_char:
                count +=1
                maxCount = max(maxCount, count)
            else:
                count = 1
            prev_char = char
        return maxCount
            
            
        