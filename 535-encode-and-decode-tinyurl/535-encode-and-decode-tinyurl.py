class Codec:
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.hash = string.ascii_letters + '0123456789'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2code:
            key = ''.join(random.choice(self.hash) for _ in range(6))
            if key not in self.code2url:
                self.code2url[key] = longUrl
                self.url2code[longUrl] = key
        
        return 'http://tinyurl.com/' + self.url2code[longUrl]
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2url[shortUrl.split('/')[-1]]   
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))