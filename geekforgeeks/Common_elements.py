import time

# def getCommon(n1, n2, n3, arr1, arr2, arr3, t):
#     i = j = k = 0
#     resDict = {}
#     res = []
#     c = 0
#     while i < n1 and j < n2 and k < n3:
#         l, m, n = i, j, k
#         c += 1
#         if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
#             if arr1[i] not in resDict:
#                 resDict[arr1[i]] = 1
#                 res.append(arr1[i])
#             i += 1
#             j += 1
#             k += 1
#         else:
#             if arr1[l] < arr2[m] or arr1[l] < arr3[n]:
#                 i += 1
#
#             if arr2[m] < arr1[l] or arr2[m] < arr3[n]:
#                 j += 1
#
#             if arr3[n] < arr1[l] or arr3[n] < arr2[m]:
#                 k += 1
#
#     if not resDict:
#         print(-1, end=" ")
#     else:
#         for i in res:
#             print(i, end=" ")
#     print()

from collections import OrderedDict


def getCommon(n1, n2, n3, arr1, arr2, arr3, t):
    h = OrderedDict()
    for i in arr1:
        if i not in h:
            h[i] = 1
    for i in arr2:
        if i in h:
            h[i] = 2
    for i in arr3:
        if i in h and h[i] == 2:
            h[i] = 3
    bool = False
    for i in h:
        if h[i] == 3:
            print(i, end=" ")
            bool = True
    if not bool:
        print(-1, end=" ")
    print()


def test():
    tcases = int(input())
    start_time = time.time()
    for t in range(tcases):
        # if t == 50:
        #     print('case no', t, (time.time() - start_time))
        #     continue
        n1, n2, n3 = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        arr3 = list(map(int, input().strip().split()))
        getCommon(n1, n2, n3, arr1, arr2, arr3, t)
    # print('case no', (time.time() - start_time))


if __name__ == "__main__":
    test()
