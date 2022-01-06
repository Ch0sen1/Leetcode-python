class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []
        
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                key += ((ord(s[i+1]) - ord(s[i]) + 26) % 26),
            dic[key].append(s)
        
        for key, value in dic.items():
            res.append(value)
            
        return res
        
        
        