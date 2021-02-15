# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        return self.dividenconq(lists, 0, len(lists) - 1)

    def dividenconq(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2

        l = self.dividenconq(lists, start, mid)
        r = self.dividenconq(lists, mid + 1, end)

        nodel = l
        noder = r
        head = None

        if nodel and noder:
            if nodel.val <= noder.val:
                head = nodel
                nodel = nodel.next
            else:
                head = noder
                noder = noder.next

        if head:
            head.next = None
        nodeh = head

        while nodel is not None and noder is not None:

            if nodel.val <= noder.val:
                nodeh.next = nodel
                nodel = nodel.next
            else:
                nodeh.next = noder
                noder = noder.next

            nodeh = nodeh.next
            nodeh.next = None

        if nodel:
            if nodeh:
                nodeh.next = nodel
            else:
                head = nodel

        if noder:
            if nodeh:
                nodeh.next = noder
            else:
                head = noder

        return head
