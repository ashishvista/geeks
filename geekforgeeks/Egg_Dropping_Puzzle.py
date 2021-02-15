# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
# def my_except_hook(exctype, value, traceback):
#     print("helooo")

#
# sys.excepthook = my_except_hook

def pascal(n, r):
    m = 1000000007
    arr = [1 for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(i - 1, 0, -1):
            arr[j] = (arr[j] % m + arr[j - 1] % m) % m
    return arr


def num_floors_covered(T, K):
    arr = pascal(T, K)
    sum = 0
    for i in range(1, min(T, K) + 1):
        sum += arr[i]
    return sum


def egg_puzzle(N, K):
    T = 0  # number of trials
    lo = 1
    high = N
    res = 0
    while lo <= high:
        mid = int((lo + high) / 2)
        nfc = num_floors_covered(mid, K)
        if nfc >= N:
            res = mid
            high = mid - 1
        elif nfc < N:
            lo = mid + 1
    return res


# print(num_floors_covered(14, 2))

if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        ### K = number of eggs , N= number of floors
        K, N = list(map(int, input().strip().split()))
        res = egg_puzzle(N, K)
        print(res)
