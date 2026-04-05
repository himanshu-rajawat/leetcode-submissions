class Node:
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_front(self, node):
        self.remove(node)
        self.add_to_front(node)
    
    def add_to_front(self, node):
        temp = self.head.next
        node.next = temp
        temp.prev = node
        node.prev = self.head
        self.head.next = node
    
    def remove_last(self):
        node = self.tail.prev
        self.remove(node)
        return node
    def remove(self, node):
        temp = node.prev
        temp.next = node.next
        node.next.prev = temp
class LRUCache:


    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}
        self.linked_list = DLL()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.linked_list.move_to_front(node)
            return node.v
        return -1
        

    def put(self, key: int, value: int) -> None:
        while len(self.cache)>=self.capacity and (key not in self.cache):
            node = self.linked_list.remove_last()
            del self.cache[node.k]
        if key not in self.cache:
            node = Node(key, value)
            self.linked_list.add_to_front(node)
        else:
            node = self.cache[key]
            node.v = value
            self.linked_list.move_to_front(node)
        self.cache[key]=node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)