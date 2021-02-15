# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        first = head
        last = head
        while last.next is not None:
            last = last.next

        return self.splitMerge(first, last)

    def splitMerge(self, first, last):
        if first == last:
            first.next = None
            return first

        mid = self.getMidNode(first, last)
        mid_next = mid.next
        lhead = self.splitMerge(first, mid)
        rhead = self.splitMerge(mid_next, last)
        return self.merge(lhead, rhead)

    def merge(self, lhead, rhead):

        head = None
        node = None
        while lhead is not None and rhead is not None:
            if lhead.val <= rhead.val:
                if head is None:
                    head = lhead
                    node = lhead
                else:
                    node.next = lhead
                    node = node.next

                lhead = lhead.next
            else:
                if head is None:
                    head = rhead
                    node = rhead
                else:
                    node.next = rhead
                    node = node.next

                rhead = rhead.next

        while lhead is not None:
            node.next = lhead
            lhead = lhead.next
            node = node.next

        while rhead is not None:
            node.next = rhead
            rhead = rhead.next
            node = node.next

        return head

    def getMidNode(self, first, last):
        node1 = first
        node2 = first
        # print("getMidNode", first.val, last.val)
        while True:
            if node2 == last or node2.next == last:
                break
            node1 = node1.next
            node2 = node2.next.next
        return node1


if __name__ == "__main__":
    arr = list(map(int, input().strip()[1:-1].split(",")))
    headd = None
    for v in arr:
        if headd is None:
            headd = ListNode(v)
            node = headd
            continue
        node.next = ListNode(v)
        node = node.next
    node = None
    res = Solution().sortList(headd)

    while res is not None:
        print(res.val, end=' ')
        res = res.next
