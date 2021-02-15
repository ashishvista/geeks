# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p = 0
    q = 0
    res = None
    found = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q

        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return 0

        l = r = found = 0
        if node == self.p or node == self.q:
            found = 1
            self.found += 1
            if self.found == 2:
                print("foundddddd", self.found)
        if self.found == 2:
            return 1

        l = self.traverse(node.left)

        if l == 3:
            return 3

        if l + found == 2:
            self.res = node
            print("llllll", node.val)

            return 3

        if self.found == 2:
            return l + r + found

        r = self.traverse(node.right)

        if r == 3:
            return 3

        if r + found == 2:
            self.res = node
            print("rrrrrrr", node.val)

            return 3

        if l + r == 2:
            self.res = node
            print("lllllrrrrr", node.val)

            return 3

        return l + r + found
