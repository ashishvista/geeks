# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        return self.sortedArrayToBSTHelper(nums, 0, n - 1, n)

    def sortedArrayToBSTHelper(self, nums, start, end, n):
        if (start > end or start < 0 or end >=n):
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTHelper(nums, start, mid - 1,n)
        node.right = self.sortedArrayToBSTHelper(nums, mid + 1, end, n)

        return node
