# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        dq = deque()
        dq.append(root)
        arr = []

        while dq:
            n = len(dq)
            tmp = []
            while n > 0:
                node = dq.popleft()
                tmp.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)
                n -= 1
            arr.append(tmp)

        return arr
