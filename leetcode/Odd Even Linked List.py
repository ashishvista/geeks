# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head

        oddHead = head
        evenHead = head.next
        even = head.next

        currOdd = oddHead.next.next

        oddHead.next = currOdd
        even.next = None
        prevOdd = oddHead
        while currOdd is not None and currOdd.next is not None:
            prevOdd = currOdd
            nextOdd = currOdd.next.next
            even.next = currOdd.next
            even = even.next
            even.next = None
            currOdd.next = nextOdd
            currOdd = currOdd.next

        if currOdd:
            currOdd.next = evenHead
        else:
            prevOdd.next = evenHead

        return oddHead
