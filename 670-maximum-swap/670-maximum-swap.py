class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        res = []
        i = 0
        
        # find the increase pivot
        while i < len(num) - 1:
            if num[i] < num[i+1]:
                break
            i += 1
        
        if i == len(num) - 1:
            return ''.join(num)
        
        # i on 2 now
        # find the biggest value we can to the right as far as we can
        max_val = num[i+1]
        max_idx = i + 1
        
        for j in range(i+1, len(num)):
            if num[j] >= max_val:
                max_val = num[j]
                max_idx = j
        
        
        # find the smallest value to the left as far as we can
        min_idx = i
        for j in range(i, -1, -1):
            if num[j] < max_val:
                min_idx = j
        
        num[max_idx], num[min_idx] = num[min_idx], num[max_idx]
        
        
        return ''.join(num)
        
                
                
        
        
                
        
        
        
        
            
        