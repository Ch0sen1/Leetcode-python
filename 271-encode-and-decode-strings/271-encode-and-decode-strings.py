class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s))
            res += ':'
            res += s
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == '':
            return None
        res = []
        i = 0
        length = 0
        
        while i < len(s):
            if s[i] != ':':
                length *= 10
                length += int(s[i])
                i += 1
            else:
                i += 1
                word = s[i:i+length]
                res.append(word)
                i += length
                length = 0
        
        return res
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))