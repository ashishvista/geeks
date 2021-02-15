import sys


def my_except_hook(exctype, value, traceback):
    print(exctype, value, traceback)


sys.excepthook = my_except_hook


def maxA(n):
    if n < 7:
        return n
    arr = [0 for i in range(n + 1)]
    for i in range(7):
        arr[i] = i
    for i in range(7, n + 1):
        arr[i] = maxAUtil(i, arr)
    return arr[n]


def maxAUtil(n, arr):
    k = 0
    for i in range(1, n - 3 + 1):
        multiplier = n - i - 1
        k = max(k, multiplier * arr[i])
    return k


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        s = maxA(n)
        print(s)
