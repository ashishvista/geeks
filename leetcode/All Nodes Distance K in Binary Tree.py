# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def distanceK2(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        h = {}
        res = []

        def traversefindtarget(node):

            if node == target:
                h[node] = 0
                return 0

            if node.left:
                res = traversefindtarget(node.left)
                if res != -1:
                    h[node] = res + 1
                    return h[node]

            if node.right:
                res = traversefindtarget(node.right)
                if res != -1:
                    h[node] = res + 1
                    return h[node]

            return -1

        def traversefindnodes(node, distance):

            if node not in h and distance > K:
                return

            if distance == K:
                res.append(node.val)

            # print(node.val, distance)

            if node.left:
                if node.left in h:
                    ldistance = h[node.left]
                else:
                    ldistance = distance + 1
                traversefindnodes(node.left, ldistance)

            if node.right:
                if node.right in h:
                    rdistance = h[node.right]
                else:
                    rdistance = distance + 1
                traversefindnodes(node.right, rdistance)

        traversefindtarget(root)

        for node in h:
            print(node.val, h[node])

        traversefindnodes(root, h[root])

        return res

    def distanceK3(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        h = {}
        res = []

        def traverse(node, parent):
            if node is None:
                return False

            if node == target:
                h[node] = parent
                return True

            if traverse(node.left, node):
                h[node] = parent
                return True

            if traverse(node.right, node):
                h[node] = parent
                return True

            return False

        traverse(root, None)
        # for node in h:
        #     print(node.val, h[node].val)

        dq = deque()

        dq.append(target)

        distance = 0
        seen = set()

        while dq:
            ln = len(dq)
            while ln > 0:
                ln -= 1
                node = dq.popleft()
                seen.add(node)

                if distance == K:
                    res.append(node.val)
                    continue

                if node.left and node.left not in seen:
                    dq.append(node.left)

                if node.right and node.right not in seen:
                    dq.append(node.right)

                if node in h and h[node] is not None and h[node] not in seen:
                    print(node.val, h[node].val)
                    dq.append(h[node])

            distance += 1

        return res

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        h = {}
        res = []

        def distanceKHelper(node):

            if node is None:
                return -1

            if node == target:
                dfs(node, 0)
                return 1

            l = distanceKHelper(node.left)

            if l != -1:
                if l == K:
                    res.append(node.val)
                    return -1
                else:
                    dfs(node.right, l + 1)
                    return l + 1

            r = distanceKHelper(node.right)

            if r != -1:
                if r == K:
                    res.append(node.val)
                    return -1
                else:
                    dfs(node.left, r + 1)
                    return r + 1

            return -1

        def dfs(node, dist):

            if node is None:
                return

            if dist == K:
                res.append(node.val)
                return

            dfs(node.left, dist + 1)
            dfs(node.right, dist + 1)

        distanceKHelper(root)
        return res
