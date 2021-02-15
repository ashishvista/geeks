# def getNthfromEnd(head, n):
#     length = 0
#     cur = head
#     while cur is not None:
#         length += 1
#         cur = cur.next
#
#     f = length - n + 1
#     if f <= 0:
#         return -1
#     c = 0
#     cur=head
#     while cur is not None:
#         c += 1
#         if c == f:
#             return cur.data
#         cur=cur.next

import sys
sys.setrecursionlimit(10**6)
def my_except_hook(exctype, value, traceback):
    print(exctype,value)

sys.excepthook = my_except_hook

# def getNthfromEnd(head, n):
#     res = getNthfromEndUtil(head, n)
#     if res['data'] is None:
#         return -1
#     else:
#         return res['data']
#
#
# def getNthfromEndUtil(head, n):
#     if head is None:
#         return {"k": 0, "data": None}
#     res = getNthfromEndUtil(head.next, n)
#     res['k'] = res['k'] + 1
#     if res['k'] == n:
#         res['data'] = head.data
#     return res

def getNthfromEnd(head, n):
    cur=head
    c=1

    while c<n:
       if cur is None:
           return -1
       c=c+1
       cur=cur.next

    while cur.next is not None:
        head=head.next
        cur=cur.next

    return head.data


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, nth_node = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getNthfromEnd(a.head, nth_node))
# } Driver Code Ends