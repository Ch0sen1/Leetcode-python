class Solution:
    # in stead of using divide, we can count the time of minus
    def divide(self, dividend, divisor):
        positive = (dividend < 1) is (divisor < 1)
        divisor = abs(divisor)
        dividend = abs(dividend)
        res = 0
        
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                res += i
                temp += temp
                i += i
                
        
        if not positive:
            res = - res
        
        return min(2**31 -1, max(-2**31 ,res))
        