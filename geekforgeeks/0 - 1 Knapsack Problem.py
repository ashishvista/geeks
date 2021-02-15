# def knapsack(arr_n, arr_w, n, w):
#     res = max(knapsack_util(arr_n, arr_w, n, w, 0, w - arr_w[0], 0 + arr_n[0]),
#               knapsack_util(arr_n, arr_w, n, w, 0, w, 0))
#     print(res)
#
#
# def knapsack_util(arr_n, arr_w, n, w, i, rw, tv):
#     if rw < 0:
#         return -1
#     if i == n - 1 or rw == 0:
#         return tv
#
#     res = max(knapsack_util(arr_n, arr_w, n, w, i + 1, rw - arr_w[i + 1], tv + arr_n[i + 1]),
#               knapsack_util(arr_n, arr_w, n, w, i + 1, rw, tv))
#
#     return res
#

# import sys
#
#
# def my_except_hook(exctype, value, traceback):
#     print("hellloo")
#
#
# sys.excepthook = my_except_hook


def knapsackTopDownDp(arr_n, arr_w, n, w):
    if w == 0:
        return 0
    total_weight = 0
    sum = 0
    for i in range(n):
        total_weight += arr_w[i]
        sum += arr_n[i]
    if w >= total_weight:
        return sum

    dp = [[-1 for i in range(w + 1)] for i in range(n + 1)]
    res = knapsackTopDownDpUtil(dp, arr_n, arr_w, n, w)
    return res
    # print(res)


def knapsackTopDownDpUtil(dp, arr_n, arr_w, n, w):
    if n == 0 or w <= 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]

    res1 = knapsackTopDownDpUtil(dp, arr_n, arr_w, n - 1, w)
    res2 = 0
    if w - arr_w[n - 1] >= 0:
        res2 = arr_n[n - 1] + knapsackTopDownDpUtil(dp, arr_n, arr_w, n - 1, w - arr_w[n - 1])
    res = max(res1, res2)
    dp[n][w] = res
    return res


def knapsackDp(arr_n, arr_w, n, w):
    if w == 0:
        return 0
    total_weight = 0
    sum = 0
    for i in range(n):
        total_weight += arr_w[i]
        sum += arr_n[i]
    if w >= total_weight:
        return sum
    dp = [[0 for i in range(w + 1)] for i in range(n + 1)]

    s = 0

    for i in range(1, n + 1):
        s += arr_w[i - 1]
        j = None
        for j in range(1, min(s + 1, w + 1)):
            diff = j - arr_w[i - 1]
            if diff >= 0:
                dp[i][j] = max(dp[i - 1][j], arr_n[i - 1] + dp[i - 1][diff])
            else:
                dp[i][j] = dp[i - 1][j]
        for k in range(j + 1, w + 1):
            dp[i][k] = dp[i][j]
    return dp[n][w]


#
# # A Dynamic Programming based Python Program for 0-1 Knapsack problem
# # Returns the maximum value that can be put in a knapsack of capacity W
# def knapSackdp2(W, wt, val, n):
#     K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#
#     # Build table K[][] in bottom up manner
#     for i in range(n + 1):
#         for w in range(W + 1):
#             if i == 0 or w == 0:
#                 K[i][w] = 0
#             elif wt[i - 1] <= w:
#                 K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
#             else:
#                 K[i][w] = K[i - 1][w]
#
#     return K[n][W]


if __name__ == "__main__":
    import time

    start = time.process_time()
    tcases = int(input())

    for t in range(tcases):
        n = int(input())
        w = int(input())
        arr_n = list(map(int, input().strip().split()))
        arr_w = list(map(int, input().strip().split()))
        # res = knapsackDp(arr_n, arr_w, n, w)
        # print(res)

        # res = knapSackdp2(w, arr_w, arr_n, n)

        res = knapsackTopDownDp(arr_n, arr_w, n, w)
        # if t == 99:
        #     print("tcase=", t, time.process_time() - start)
        print(res)
