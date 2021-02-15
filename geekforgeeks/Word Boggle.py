from collections import defaultdict


def boggle(m, n, arr, str_arr, k, h):
    ans = []
    ansHash = {}
    directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    visited = [[False for i in range(n)] for i in range(m)]
    for s in str_arr:
        coords = h[s[0]]
        for coord in coords:
            if s not in ansHash and dfsUtil(m, n, arr, coord[0], coord[1], 0, directions, visited, s):
                ans.append(s)
                ansHash[s] = 1
                break
    ans.sort()
    if len(ans) == 0:
        print(-1, end=" ")
    for s in ans:
        print(s, end=" ")


def dfsUtil(m, n, arr, i, j, index, directions, visited, s):
    if index == len(s) - 1:
        return True

    visited[i][j] = True
    for d in directions:
        x = i + d[0]
        y = j + d[1]
        # ch1 = arr[x][y]
        # ch2 = s[index + 1]
        if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and arr[x][y] == s[index + 1]:
            if dfsUtil(m, n, arr, x, y, index + 1, directions, visited, s):
                visited[i][j] = False
                return True
    visited[i][j] = False
    return False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        k = int(input())
        str_arr = input().strip().split(" ")
        m, n = list(map(int, input().strip().split()))
        temp = input().strip().split()
        c = 0
        arr = []
        h = defaultdict(list)
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(temp[c])
                h[temp[c]].append([i, j])
                c += 1
            arr.append(tmp)
        boggle(m, n, arr, str_arr, k, h)
        print()
