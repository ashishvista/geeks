def mcmTD(n, arr, low, high, dp):
    if dp[low][high] > -1:
        return dp[low][high]
    if low == high:
        return 0

    min = float("inf")
    for i in range(low, high):
        mid = i
        ops = mcmTD(n, arr, low, mid, dp) + mcmTD(n, arr, mid + 1, high, dp) + arr[low - 1] * \
              arr[mid] * arr[high]

        if ops < min:
            min = ops
    dp[low][high] = min
    return min


def mcmBU(n, arr):
    num_of_matrx = n - 1
    dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1, num_of_matrx):
        for j in range(1, num_of_matrx):
            low = j
            high = j + i
            if high > num_of_matrx:
                break
            min = float("inf")
            for k in range(low, high):
                mid = k
                ops = dp[low][mid] + dp[mid + 1][high] + arr[low - 1] * arr[mid] * arr[high]

                if ops < min:
                    min = ops
            dp[low][high] = min

    return dp[1][num_of_matrx]


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        dp = [[-1 for i in range(n + 1)] for i in range(n + 1)]
        # res = mcmTD(n, arr, 1, n - 1, dp)  # tle more than 38 test cases
        res = mcmBU(n, arr)  # tle more than 64 test cases
        if t == 64:
            print("hello")
            break
        print(res)
