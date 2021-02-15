"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        self.connectHelper(root.left, None)
        self.connectHelper(root.right, root.left)
        return root

    def connectHelper(self, node, knode):
        if node is None:
            return
        if knode is not None:
            knode.next = node
            knode = knode.right

        self.connectHelper(node.left, knode)
        self.connectHelper(node.right, node.left)
