def findPath():
    arr = [[0 for i in range(4)] for i in range(4)]
    findPathUtil(arr, 3, 0, [], 0)


def findPathUtil(arr, i, j, path, c):
    if arr[i][j] == 1:
        return False
    arr[i][j] = 1
    c = c + 1
    temp = list(path)
    temp.append([i, j])
    if i == 0 and j == 3 and c==9:
        print(temp, c)
    if isSafe(arr, i, j - 1):
        findPathUtil(arr, i, j - 1, list(temp), c)

    if isSafe(arr, i - 1, j):
        findPathUtil(arr, i - 1, j, list(temp), c)

    if isSafe(arr, i, j + 1):
        findPathUtil(arr, i, j + 1, list(temp), c)

    if isSafe(arr, i + 1, j):
        findPathUtil(arr, i + 1, j, list(temp), c)

    arr[i][j] = 0


def isSafe(arr, i, j):
    if i < 0 or i > 3 or j < 0 or j > 3 or arr[i][j] == 1:
        return False
    return True


findPath()
