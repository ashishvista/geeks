from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dq = deque([root, None])
        prev = None
        arr = []
        if root is None:
            return arr

        while dq:
            node = dq.popleft()
            if node is None:
                arr.append(prev.val)
                if dq:
                    dq.append(None)
                else:
                    break
                continue
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            prev = node

        return arr
