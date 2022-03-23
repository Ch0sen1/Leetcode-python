class Solution:
    def brokenCalc(self, X, Y):
        res = 0
        while X != Y:
            if Y < X:
                res += (X-Y)
                break
            else:
                if Y%2 == 0:
                    Y = Y//2
                else:
                    Y = Y+1
                res += 1
        return res
                
            
            
        