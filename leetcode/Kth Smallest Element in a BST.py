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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return []
        st = []
        c = 0
        while True:
            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            c += 1
            if c == k:
                return root.val
            root = root.right


if __name__ == "__main__":
    arr = input().strip()[1:-1].split(",")
    k = int(input())
    root = deserialize(arr)
    res = Solution().kthSmallest(root, k)
    print(res)
