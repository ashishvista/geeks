# This function should rotate list counter-
# clockwise by k and return new head (if changed)
def rotateList(head, k):
    tmp = head
    c = 0
    while tmp is not None:
        c = c + 1
        lastNode = tmp
        tmp = tmp.next

    k = k % c
    if k == 0:
        return head

    tmp = head
    for i in range(k - 1):
        tmp = tmp.next

    newTail = tmp
    newHead = tmp.next

    lastNode.next = head
    newTail.next = None
    return newHead


# {
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa

# } Driver Code Ends

print("abcd")