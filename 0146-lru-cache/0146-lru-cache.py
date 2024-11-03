class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self,node):
        prev_right = self.right.prev
        prev_right.next, self.right.prev = node,node
        node.prev, node.next = prev_right, self.right
    def remove(self,node):
        node_left, node_right = node.prev, node.next
        node_left.next, node_right.prev = node_right, node_left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            least_used = self.left.next
            self.remove(least_used)
            del self.cache[least_used.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)