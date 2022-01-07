class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = Counter()
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.addToHead(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.addToHead(node)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.addToHead(node)
            
            
        
        
    
    def addToHead(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        node = self.tail.prev
        del self.dic[node.key]
        self.remove(node)
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)