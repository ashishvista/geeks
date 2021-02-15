# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        t1 = head
        t2 = head
        while t2 is not None and t2.next is not None:
            t1 = t1.next
            t2 = t2.next.next
        t1 = self.reverseList(t1)
        t2 = head
        while t1 is not None and t2 is not None:
            if t1.val != t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return True

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
