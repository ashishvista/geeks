class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


def prepareLinkedList(n, arr):
    head = Node(arr[0])
    cur = head
    c = 1
    while c < len(arr):
        temp = Node(arr[c])
        cur.next = temp
        cur = cur.next
        c += 1
    return head


def seggregate(head):
    cur = head
    while cur.next is not None:
        cur = cur.next
    last = cur
    end = last
    cur = head

    prev = None
    while cur.next is not None:
        flag = False
        if cur == last:
            flag = True
        if cur.data % 2 == 1:
            temp = cur
            cur = cur.next
            temp.next = None
            end.next = temp
            end = temp
            if prev is None:
                head = cur
            else:
                prev.next = cur
        else:
            prev = cur
            cur = cur.next
        if flag:
            return head
    return head


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = prepareLinkedList(n, arr)
        cur=seggregate(head)
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()
