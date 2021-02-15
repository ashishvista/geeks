# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        arr = self.robHelper(root)
        return max(arr[0], arr[1])

    def robHelper(self, node):
        if node is None:
            return [0, 0]

        arr1 = self.robHelper(node.left)
        cur_inc1 = arr1[1] + node.val
        cur_exc1 = max(arr1[0], arr1[1])

        arr2 = self.robHelper(node.right)

        cur_inc2 = arr2[1] + node.val
        cur_exc2 = max(arr2[0], arr2[1])

        cur_inc = max(cur_inc1 + arr2[1], cur_inc2 + arr1[1])
        cur_exc = cur_exc1 + cur_exc2

        if node.val == 4:
            print([cur_inc, cur_exc])
        return [cur_inc, cur_exc]
