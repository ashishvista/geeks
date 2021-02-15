# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp1 = l1
        tmp2 = l2
        tmp3 = None
        l3 = None
        e = 0

        while tmp1 or tmp2:

            if tmp1 and tmp2:
                val = tmp1.val + tmp2.val + e
                tmp1 = tmp1.next
                tmp2 = tmp2.next

            elif tmp1:
                val = tmp1.val + e
                tmp1 = tmp1.next

            elif tmp2:
                val = tmp2.val + e
                tmp2 = tmp2.next

            e = val // 10
            r = val % 10
            if not tmp3:
                tmp3 = ListNode(r)
                l3 = tmp3
            else:
                tmp3.next = ListNode(r)
                tmp3 = tmp3.next

        if e == 1:
            tmp3.next = ListNode(e)

        return l3


def printList(l):
    tmp = l
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next


def convertToList(l):
    list = None
    temp = None
    for v in l:
        if not list:
            list = ListNode(v)
            temp = list
        else:
            temp.next = ListNode(v)
            temp = temp.next
    return list


if __name__ == "__main__":
    l1 = map(int, input()[1: -1].strip().split(','))
    l2 = map(int, input()[1: -1].strip().split(','))
    l1 = convertToList(l1)
    l2 = convertToList(l2)
    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    printList(l3)
