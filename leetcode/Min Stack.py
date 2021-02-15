class Node:
    def __init__(self, x, minV, next):
        self.x = x
        self.minV = minV
        self.next = next


class MinStack:
    head = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:

        if self.head is None:
            self.head = Node(x, x, None)
        else:
            self.head = Node(x, min(x, self.head.minV), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.x

    def getMin(self) -> int:
        return self.head.minV

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
