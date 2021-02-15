# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = deque([root])
        right = deque([root])
        while left:
            l = left.popleft()
            r = right.popleft()

            l1 = l.left
            l2 = l.right

            r1 = r.right
            r2 = r.left
            if (l1 and r1) and l1.val == r1.val:
                left.append(l1)
                right.append(r1)
            elif not l1 and not r1:
                print()
            else:
                return False

            if (l2 and r2) and l2.val == r2.val:
                left.append(l2)
                right.append(r2)
            elif not l2 and not r2:
                print()
            else:
                return False

        return True
