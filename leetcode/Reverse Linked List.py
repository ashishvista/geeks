# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        t1 = head.next
        head.next = None
        while t1 is not None:
            t2 = t1.next
            t1.next = head
            head = t1
            t1 = t2
        return head
