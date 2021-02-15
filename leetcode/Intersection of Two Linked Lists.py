# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        elif headA == headB:
            return headA
        ta = headA
        tb = headB
        reached = 0
        lastA = None
        lastB = None
        while ta != tb:
            if ta.next is None:
                reached += 1
                lastA = ta
                ta = headB

            else:
                ta = ta.next

            if tb.next is None:
                reached += 1
                lastB = tb
                tb = headA

            else:
                tb = tb.next

            if reached == 2 and lastA != lastB:
                print("reached", ta.val, tb.val)
                return None

            if ta == tb:
                return ta





