class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.capacity=capacity

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self,node:Node) -> None:
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def _addToFront(self, node:Node) -> None:
        first=self.head.next
        node.next=first
        node.prev=self.head
        self.head.next=node
        first.prev=node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._addToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node=self.map[key]
            node.val=value
            self._remove(node)
            self._addToFront(node)
            return
        node=Node(key,value)
        self.map[key] = node
        self._addToFront(node)

        if len(self.map)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)