class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True
        
        

    def search(self, word: str) -> bool:
        
        
        def dfs(i, node):
            if i == len(word):
                return node.isWord
            
            if word[i] == '.':
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
            if word[i] in node.children:
                return dfs(i+1, node.children[word[i]])
            
            return False
            
        
        return dfs(0, self.root)
            
            
    
    
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)