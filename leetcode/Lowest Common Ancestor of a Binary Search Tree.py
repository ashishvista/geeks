# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lca = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.traverse(root, p, q)
        return self.lca

    def traverse(self, node, p, q):
        if p.val < node.val and q.val < node.val:
            self.lowestCommonAncestor(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            self.lowestCommonAncestor(node.right, p, q)
        else:
            self.lca = node
            return
