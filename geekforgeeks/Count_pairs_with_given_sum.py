import sys

NN = 0
SUM = 0


def my_except_hook(exctype, value, traceback):
    global NN
    global SUM
    print(NN, SUM, exctype, value, traceback)


sys.excepthook = my_except_hook

sys.setrecursionlimit(10 ** 6)


#
# def get_num_pairs(n, sum, arr):
#     h = {}
#     pairs = 0
#     for item in arr:
#         if item not in h:
#             h[item] = 1
#         else:
#             h[item] += 1
#
#     for item in h:
#         remaining = sum - item
#         if item == remaining and h[item] > 0:
#             N = h[item]
#             if N > 1:
#                 a = factorial(N)
#                 b = factorial(N - 2)
#                 res = a / (2 * b)
#                 pairs += int(res)
#                 h[item] = 0
#         elif h[item] > 0 and remaining in h and h[remaining] > 0:
#             pairs = pairs + (h[item] * h[remaining])
#             h[item] = h[remaining] = 0
#     return pairs

def get_num_pairs(n, sum, arr):
    h = {}
    pairs = 0
    for item in arr:
        if item not in h:
            h[item] = 1
        else:
            h[item] += 1

    for item in arr:
        remaining = sum - item
        if remaining in h:
            if remaining == item:
                pairs += h[remaining] - 1
            else:
                pairs += h[remaining]

    return int(pairs / 2)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     res = n * factorial(n - 1)
#     return res
#

if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, sum = list(map(int, input().strip().split()))
        NN = n
        SUM = sum
        arr = list(map(int, input().strip().split()))
        pairs = get_num_pairs(n, sum, arr)
        print(pairs)
