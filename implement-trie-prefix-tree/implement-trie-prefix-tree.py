class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)
        
        
    def dfs(self, node, word):
        if not word:
            return node.endWord
        if word[0] in node.children:
            return self.dfs(node.children[word[0]], word[1:])
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False
        return True
    
    
        
        
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)