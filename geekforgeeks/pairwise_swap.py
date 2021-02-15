# def pairWiseSwap(head):
#     prev = Node(-1)
#     prev.next = head
#
#     if head is None or head.next is None:
#         return head
#
#     head = head.next
#
#     while True:
#         if prev.next is None or prev.next.next is None:
#             break
#
#         cur = prev.next
#         next = prev.next.next
#
#         prev.next = next
#         cur.next = next.next
#         next.next = cur
#
#         prev = prev.next.next
#
#     return head

def pairWiseSwap(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next
    remaining = head.next.next

    second.next = first
    first.next = pairWiseSwap(remaining)

    return second


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        llist.head = pairWiseSwap(llist.head)
        llist.printList()
        t -= 1
