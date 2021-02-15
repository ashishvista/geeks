from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.h = defaultdict(int)

        self.pathSumHelper(root, 0, sum)
        return self.count

    def pathSumHelper(self, root, acc_sum, sum):
        if root is None:
            return

        acc_sum += root.val

        self.h[acc_sum] += 1

        if acc_sum == sum:
            self.count += 1

        remaining = acc_sum - sum
        self.count += self.h[remaining]

        self.pathSumHelper(root.left, acc_sum, sum)
        self.pathSumHelper(root.right, acc_sum, sum)

        self.h[acc_sum] -= 1
