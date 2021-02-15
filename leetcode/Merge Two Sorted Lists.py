# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        head = None
        curr3 = None
        while curr1 is not None and curr2 is not None:

            if curr1.val <= curr2.val:
                if head is None:
                    head = curr1
                    curr3 = curr1
                else:
                    curr3.next = curr1
                    curr3 = curr3.next

                curr1 = curr1.next
            else:
                if head is None:
                    head = curr2
                    curr3 = curr2
                else:
                    curr3.next = curr2
                    curr3 = curr3.next

                curr2 = curr2.next

        while curr1 is not None:
            if head is None:
                head = curr1
                curr3 = curr1
            else:
                curr3.next = curr1
                curr3 = curr3.next
            curr1 = curr1.next
        while curr2 is not None:
            if head is None:
                head = curr2
                curr3 = curr2
            else:
                curr3.next = curr2
                curr3 = curr3.next
            curr2 = curr2.next

        return head
