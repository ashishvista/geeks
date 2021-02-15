def detectLoop(head):
    h = {}
    while head.next != None:
        if head in h:
            return True
        else:
            h[head] = 1
        head = head.next
    return False


# code here


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # connects last node to node at position pos from begining.

    def add(self, pos):
        last = self.head
        while last.next:
            last = last.next
        pos = pos - 1;
        temp = self.head
        while pos:
            temp = temp.next
            pos -= 1
        last.next = temp

        return


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))

        for x in nodes_a:
            a.push(x)
        loop = int(input())
        if (loop):
            a.add(loop)
        print(detectLoop(a.head))
# } Driver Code Ends
