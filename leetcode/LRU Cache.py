class Node:
    next = None
    prev = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.capacity = capacity
        self.front = None
        self.last = None

    def get(self, key: int) -> int:
        if key in self.h:
            node = self.h[key]
            self.deleteNode(node)
            self.putNodeAtFront(node)
            return node.value
        else:
            return -1

    def printDeque(self):
        node = self.front
        while node:
            print("pp", node.value)
            node = node.next

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h[key].value = value
            node = self.h[key]
            self.deleteNode(node)
            self.putNodeAtFront(node)
        else:
            if len(self.h) == self.capacity:
                del self.h[self.last.key]
                self.deleteNode(self.last)

            node = Node(key, value)
            self.putNodeAtFront(node)
            self.h[key] = node

    def deleteNode(self, node):
        if self.front == node:
            if self.front.next is None:
                self.front = None
                self.last = None
            else:
                self.front = self.front.next
                self.front.prev = None
        elif self.last == node:
            tmp = self.last.prev
            tmp.next = None
            self.last = tmp
        else:
            tmp1 = node.prev
            tmp2 = node.next
            tmp1.next = tmp2
            tmp2.prev = tmp1

        node.prev = node.next = None

    def putNodeAtFront(self, node):
        if not self.front:
            self.last = self.front = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
