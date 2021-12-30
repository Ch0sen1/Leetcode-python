class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l = 0
        r = len(num) - 1
        dic = {"1":"1", 
              "0":"0",
              "6":"9",
              "8":"8",
              "9":"6"}
        while l <= r:
            if num[l] not in dic:
                return False
            else:
                if num[r] == dic[num[l]]:
                    l += 1
                    r -= 1
                else:
                    return False
        
        return True
        