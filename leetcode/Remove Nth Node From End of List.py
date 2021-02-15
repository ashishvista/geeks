# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = 1
        node1 = head

        while tmp < n:
            node1 = node1.next
            tmp += 1

        node2 = head
        prev = None
        while node1.next is not None:
            node1 = node1.next
            prev = node2
            node2 = node2.next

        if prev is None:
            head = head.next
        else:
            prev.next = node2.next

        return head
