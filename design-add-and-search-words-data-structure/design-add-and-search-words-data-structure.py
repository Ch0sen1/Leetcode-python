class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)