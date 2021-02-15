from collections import defaultdict


class Node:
    def __init__(self, s, i):
        self.s = s
        self.i = i


def isCircle(n, arr):
    node_arr = []
    h = defaultdict(list)
    for i, s in enumerate(arr):
        node = Node(s, i)
        h[s[0]].append(node)
        node_arr.append(node)

    visited = {node_arr[0]: 1}
    circle_arr = []
    res = isCircleUtil(n, arr, h, node_arr[0], visited, 1, node_arr[0], circle_arr)
    if res:
        print(1)
    else:
        print(0)


def isCircleUtil(n, arr, h, cur_node, visited, count, root_node, circle_arr):
    visited[cur_node] = 1
    circle_arr.append(cur_node.s)
    cur_s = cur_node.s
    cur_indx = cur_node.i
    lst_indx = len(cur_s) - 1
    ch = cur_s[lst_indx]
    if count == n and ch == root_node.s[0]:
        # print(circle_arr)
        return True

    for node in h[ch]:
        if node not in visited and isCircleUtil(n, arr, h, node, visited, count + 1, root_node, circle_arr):
            return True

    circle_arr.pop()
    del visited[cur_node]
    return False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = input().strip().split()
        isCircle(n, arr)
