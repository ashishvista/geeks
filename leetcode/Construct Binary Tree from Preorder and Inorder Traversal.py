# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        self.preorder = preorder
        n = len(self.preorder)
        self.inorder = inorder
        self.pindex = 0
        self.hash = {}
        for i in range(n):
            self.hash[inorder[i]] = i
        root = TreeNode(self.preorder[self.pindex])
        # index = self.searchArr(0, n - 1, self.preorder[self.pindex])
        index = self.hash[self.preorder[self.pindex]]

        self.pindex += 1
        root.left = self.buildTreeHelper(0, index - 1)
        root.right = self.buildTreeHelper(index + 1, n - 1)
        return root

    def buildTreeHelper(self, start, end) -> TreeNode:
        if start > end:
            return None

        node = TreeNode(self.preorder[self.pindex], None, None)
        # index = self.searchArr(start, end, self.preorder[self.pindex])
        index = self.hash[self.preorder[self.pindex]]
        self.pindex += 1
        node.left = self.buildTreeHelper(start, index - 1)
        node.right = self.buildTreeHelper(index + 1, end)
        return node

    def searchArr(self, i, j, num):
        for k in range(i, j + 1):
            if num == self.inorder[k]:
                return k
