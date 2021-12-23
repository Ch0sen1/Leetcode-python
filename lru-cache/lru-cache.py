class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove_from_list(node)
            self.insert_to_head(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove_from_list(node)
            self.insert_to_head(node)
            node.value = value
        else:
            if len(self.dic) >= self.capacity:
                self.remove_from_tail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insert_to_head(node)
              
    def insert_to_head(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node
    
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
      
    
    def remove_from_tail(self):
        if len(self.dic) == 0:
            return
        node = self.tail.prev
        del self.dic[node.key]
        self.remove_from_list(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)