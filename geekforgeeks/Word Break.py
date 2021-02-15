import sys

sys.setrecursionlimit(10 ** 6)


def wordbreak(arr, w):
    h = {}
    for word in arr:
        h[word] = 1

    if wordbreakUtil(h, w, 0, len(w) - 1):
        return 1
    else:
        return 0


def wordbreakUtil(h, w, s, e):
    if s > e:
        return True
    tmp = w[s:e + 1]
    if tmp in h:
        return True

    if e == s:
        return False

    start = s
    mid = s
    end = e
    while mid < end:
        if wordbreakUtil(h, w, start, mid) and wordbreakUtil(h, w, mid + 1, end):
            return True
        mid += 1
    return False


def wordbreak2(arr, w):
    h = {}
    word_length = len(w)
    dp = [[False for i in range(word_length)] for i in range(word_length)]
    for word in arr:
        h[word] = 1

    start = 0
    size = 1
    end = len(w) - 1

    while size <= word_length:
        while start <= word_length - size:
            s = start
            e = start + size - 1
            dp[s][e] = wordbreakUtil2(h, w, s, e, dp)
            start += 1
        start = 0
        size += 1

    if dp[0][word_length - 1]:
        return 1
    else:
        return 0

def wordbreakUtil2(h, w, s, e, dp):
    tmp = w[s:e + 1]
    if tmp in h:
        return True

    if e == s:
        return False

    start = s
    mid = s
    end = e
    while mid < end:
        if dp[start][mid] and dp[mid + 1][end]:
            return True
        mid += 1
    return False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = input().strip().split()
        w = input()
        res = wordbreak2(arr, w)
        print(res)
