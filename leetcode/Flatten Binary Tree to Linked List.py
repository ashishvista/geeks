# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    last = None

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        self.last = root
        self.flatten(root.left)
        temp = root.right
        root.right = root.left
        root.left = None
        self.last.right = temp
        self.flatten(temp)
