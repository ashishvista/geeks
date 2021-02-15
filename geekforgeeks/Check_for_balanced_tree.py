# User function Template for python3


'''class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None'''


# This function should return tree if passed  tree
# is balanced, else false.  Time complexity should
# be O(n) where n is number of nodes in tree */
def isBalanced(root):
    h = countheight(root, 0)
    if h == -1:
        return False
    else:
        return True


def countheight(node, h):
    if node is None:
        return h
    t1 = countheight(node.left, h + 1)
    if t1 == -1:
        return -1
    t2 = countheight(node.right, h + 1)
    if t2 == -1:
        return -1

    if abs(t1 - t2) > 1:
        return -1

    return max(t1, t2)


# add code here


# {
#  Driver Code Starts
# Initial Template for Python 3

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        if isBalanced(root):
            print(1)
        else:
            print(0)
# } Driver Code Ends
