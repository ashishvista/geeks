# User function Template for python3

'''
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.pre=None
'''


class LRUCache:
    hsmap = dict()
    capacity = count = 0
    head = tail = None

    def __init__(self, cap):
        self.hsmap = dict()
        self.capacity = self.count = 0
        self.capacity = cap
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.special = "head"
        self.tail.special = "tail"

        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.hsmap:
            item = self.hsmap[key]
            self.deleteNode(item)
            self.pushNode(item)
            return item.value
        else:
            return -1

    def set(self, key, value):
        if key in self.hsmap:
            item = self.hsmap[key]
            item.value = value
            self.deleteNode(item)
            self.pushNode(item)

        else:
            if self.count < self.capacity:
                node = Node(key, value)
                self.hsmap[key] = node
                self.pushNode(node)
            else:
                self.deleteLastNode()
                node = Node(key, value)
                self.hsmap[key] = node
                self.pushNode(node)

    def deleteNode(self, node):
        left = node.pre
        right = node.next
        left.next = right
        right.pre = left
        self.count -= 1

    def pushNode(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node
        self.count += 1

    def deleteLastNode(self):
        dnode = self.tail.pre
        try:
            dnode.pre.next = self.tail
        except:
            print(dnode)
        self.tail.pre = dnode.pre
        del self.hsmap[dnode.key]
        self.count -= 1


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.pre = None


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends
