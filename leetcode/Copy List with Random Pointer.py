"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':

        if head is None:
            return None
        curr1 = head
        head2 = None
        prev2 = None

        while curr1 is not None:

            curr2 = Node(curr1.val, None, curr1)

            if head2 is None:
                head2 = curr2
            if prev2 is not None:
                prev2.next = curr2
            prev2 = curr2
            curr1_next = curr1.next
            curr1.next = curr2
            curr1 = curr1_next

        curr2 = head2
        while curr2 is not None:
            if curr2.random.random is not None:
                curr2.random = curr2.random.random.next
            else:
                curr2.random = None
            curr2 = curr2.next
        return head2

    def copyRandomList(self, head: 'Node') -> 'Node':

        if head is None:
            return None
        curr1 = head
        head2 = None
        prev2 = None

        while curr1 is not None:
            curr2 = Node(curr1.val, None, None)
            curr1_next = curr1.next
            curr1.next = curr2
            curr2.next = curr1_next
            curr1 = curr1_next

        head2 = head.next

        curr1 = head

        while curr1 is not None:
            print(curr1.val)
            if curr1.random is not None:
                curr1.next.random = curr1.random.next
            curr1 = curr1.next.next

        curr1 = head
        curr2 = head2

        while curr2 is not None:
            curr1.next = curr2.next
            curr1 = curr2
            curr2 = curr2.next
        return head2
