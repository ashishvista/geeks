# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:
    ss = ""

    def deserializeOriginal(self, arr):
        n = len(arr)
        dq = deque()
        if n == 0:
            return None
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

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.ss = ""
        if root is None:
            return self.ss
        self.serializeHelper(root)
        return self.ss

    def serializeHelper(self, node):
        if node is None:
            self.ss += "null" + " "
            return

        self.ss += str(node.val) + " "
        self.serializeHelper(node.left)
        self.serializeHelper(node.right)

    def deserialize1(self, data):
        if data == "":
            return None
        arr = data.strip().split(" ")
        node = TreeNode(int(arr[0]))
        root = node
        st = [node]
        n = len(arr)
        i = 1
        while i < n:

            if arr[i] != "null":
                node.left = TreeNode(int(arr[i]))
                node = node.left
                st.append(node)
                i += 1

            else:
                i += 1
                if st:
                    node = st.pop()
                if i < n and arr[i] != "null":
                    node.right = TreeNode(int(arr[i]))
                    node = node.right
                    st.append(node)
                    i += 1
        return root

    def deserialize(self, data):
        if data == "":
            return None
        arr = data.strip().split(" ")
        self.i = 0
        root = TreeNode(int(arr[0]))
        root.left = self.deserializeHelper(arr)
        root.right = self.deserializeHelper(arr)
        return root

    def deserializeHelper(self, arr):
        self.i += 1
        if arr[self.i] == "null":
            return None

        node = TreeNode(int(arr[self.i]))
        node.left = self.deserializeHelper(arr)
        node.right = self.deserializeHelper(arr)
        return node


if __name__ == "__main__":
    arr = input().strip()[1:-1].split(",")
    s = Codec()
    root = s.deserializeOriginal(arr)
    data = s.serialize(root)
    res = s.deserialize(data)
    print(data)
