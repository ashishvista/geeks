def perm(s):
    n = len(s)
    ss = sorted(s)
    permS = []
    ssIndexArr = [0 for i in range(n)]
    h = {}
    for i in range(n):
        permUtil(ss, ssIndexArr, i, permS, n - 1, n, h)


def permUtil(ss, ssIndexArr, index, permS, remaining, n, h):
    ssIndexArr[index] = 1
    permS.append(ss[index])

    if remaining == 0:
        tmp = "".join(permS)
        if tmp not in h:
            h[tmp] = 1
            print(tmp, end=" ")

    for i in range(n):
        if ssIndexArr[i] == 0:
            permUtil(ss, ssIndexArr, i, permS, remaining - 1, n, h)

    ssIndexArr[index] = 0
    permS.pop()


def perm2(s):
    arr = sorted(s)
    n = len(s)
    res = []
    permUtil2(arr, 0, n, res)
    res.sort()
    for i in res:
        print(i, end=" ")


def permUtil2(arr, start, n, res):
    if start == n - 1:
        # print("".join(arr), end=" ")
        res.append("".join(arr))
        return

    for i in range(start, n):
        arr[start], arr[i] = arr[i], arr[start]
        permUtil2(arr, start + 1, n, res)
        arr[start], arr[i] = arr[i], arr[start]


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        s = input()
        perm2(s)
        print()
