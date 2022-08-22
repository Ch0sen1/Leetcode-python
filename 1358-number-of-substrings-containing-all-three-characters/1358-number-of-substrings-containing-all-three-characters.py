class Solution:
    
    
    def numberOfSubstrings(self, s: str) -> int:
        def atMostK(s, k):
            l = r = res = 0
            dic = Counter()
            while r < len(s):
                w = s[r]
                dic[w] += 1
                while len(dic) > k:
                    dic[s[l]] -= 1
                    if dic[s[l]] == 0:
                        del dic[s[l]]
                    l += 1
                res += r-l+1
                r += 1

            return res
    
    
        return atMostK(s,3) - atMostK(s,2)
        
        
        