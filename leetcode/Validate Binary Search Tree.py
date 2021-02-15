# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(arr):
    n = len(arr)
    dq = deque()
    root = TreeNode(int(arr[0]))
    dq.append(root)
    i = 1
    while dq:
        top = dq.popleft()
        if i < n:
            if arr[i] != "null":
                top.left = TreeNode(int(arr[i]))
                dq.append(top.left)
        if (i + 1) < n:
            if arr[i + 1] != "null":
                top.right = TreeNode(int(arr[i + 1]))
                dq.append(top.right)
        i += 2
    return root


class Solution:
    prev = float("-inf")

    def isValidBST1(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isValidBSTHelper(root, float("inf"), float("-inf"))

    def isValidBSTHelper(self, node, ll, lr):

        if node is None:
            return True

        if not (node.val < ll and node.val > lr):
            return False

        return self.isValidBSTHelper(node.left, node.val, lr) and self.isValidBSTHelper(node.right, ll, node.val)

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.inorderTraverse(root)

    def inorderTraverse(self, node: TreeNode) -> bool:
        if node is None:
            return True

        l = self.inorderTraverse(node.left)
        if not l:
            return False

        if node.val <= self.prev:
            return False
        else:
            self.prev = node.val

        r = self.inorderTraverse(node.right)
        if not r:
            return False
        return True


if __name__ == "__main__":
    arr = input().strip()[1:-1].split(",")
    root = deserialize(arr)
    res = Solution().isValidBST(root)
    print(res)
