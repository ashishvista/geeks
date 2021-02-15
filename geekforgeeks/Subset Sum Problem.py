def isSubsetSum(n, arr):
    s = 0
    for i in arr:
        s += i
    if s % 2 != 0:
        res = False
    else:
        res = isSubsetSumUtil(n, arr, s // 2, [])

    if res:
        print("YES")
    else:
        print("NO")


def isSubsetSumUtil(n, arr, s, tmp):
    if n >= 0 and s == 0:
        # print(tmp)
        return True
    if n == 0 and s != 0:
        return False
    tmp1 = list(tmp)
    tmp2 = list(tmp)
    tmp2.append(arr[n - 1])

    return isSubsetSumUtil(n - 1, arr, s, tmp1) or isSubsetSumUtil(n - 1, arr, s - arr[n - 1], tmp2)


def isSubsetSumDp(n, arr):
    s = 0
    for i in arr:
        s += i
    if s == 0:
        print("YES")
        return
    if s % 2 != 0:
        print("NO")
        return
    s = s // 2
    dp = [[0 for i in range(s + 1)] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1

    if arr[0] <= s:
        dp[0][arr[0]] = 1
    ysum = arr[0]
    for i in range(1, n):
        ysum += arr[i]
        for j in range(1, min(ysum + 1, s + 1)):
            diff = j - arr[i]
            if dp[i - 1][j] == 1 or (diff >= 0 and dp[i - 1][diff] == 1):
                dp[i][j] = 1
    if dp[i][s] == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        isSubsetSumDp(n, arr)
