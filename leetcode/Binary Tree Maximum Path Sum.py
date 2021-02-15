# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxx = [float("-inf")]
        maxx_node = [float("-inf")]
        self.helper(root, maxx, maxx_node)
        if maxx_node[0] < 0:
            return maxx_node[0]
        
        return maxx[0]

    def helper(self, root, maxx, maxx_node):
        if root is None:
            return 0
        l = self.helper(root.left, maxx, maxx_node)
        r = self.helper(root.right, maxx, maxx_node)

        maxx[0] = max(l + r + root.val, maxx[0])

        mxlr = max(l, r)
        maxx[0] = max(mxlr, maxx[0])
        mxlr_root = max(mxlr + root.val, root.val, 0)
        maxx[0] = max(mxlr + root.val, root.val, maxx[0])
        maxx_node[0] = max(maxx_node[0], root.val)
        # if maxx[0] == 55:
        #     print(root.val)
        return mxlr_root
