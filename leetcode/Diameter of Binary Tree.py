# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    dia = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.helper(root)
        return self.dia - 1

    def helper(self, node):
        if node is None:
            return 0
        l = self.helper(node.left)
        r = self.helper(node.right)

        sum = l + r + 1
        self.dia = max(self.dia, sum)
        return max(l, r) + 1
