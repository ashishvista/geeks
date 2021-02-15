# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.mergeTreesHelper(t1, t2)

    def mergeTreesHelper1(self, t1, t2):

        if t1 is None and t2 is None:
            return None
        v1 = v2 = 0

        if t1 is not None:
            v1 = t1.val

        if t2 is not None:
            v2 = t2.val

        t3 = TreeNode(v1 + v2)

        t1Left = t1Right = t2Left = t2Right = None

        if t1:
            t1Left = t1.left
            t1Right = t1.right

        if t2:
            t2Left = t2.left
            t2Right = t2.right

        l = self.mergeTreesHelper(t1Left, t2Left)
        t3.left = l

        r = self.mergeTreesHelper(t1Right, t2Right)
        t3.right = r

        return t3

    def mergeTreesHelper(self, t1, t2):

        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val = t1.val + t2.val

        t1.left = self.mergeTreesHelper1(t1.left, t2.left)
        t1.right = self.mergeTreesHelper1(t1.right, t2.right)

        return t1
