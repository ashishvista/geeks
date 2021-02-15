from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        def compare(a):
            return a[0]

        people = sorted(people, key=lambda x: (x[0], x[1] * -1), reverse=True)
        head = None
        for v in people:
            if head is None:
                head = ListNode(v)
            else:
                tmp = v[1]
                node = head
                if tmp == 0:
                    head = ListNode(v, head)
                    continue
                while True:
                    if tmp == 1:
                        node.next = ListNode(v, node.next)
                        break
                    else:
                        node = node.next
                        tmp -= 1

        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people = sorted(people, key=lambda x: (x[0], x[1] * -1), reverse=True)
        res = []
        for v in people:
            res.insert(v[1], v)

        return res


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split(","))))
    s = Solution().reconstructQueue(arr)
    print(s)
