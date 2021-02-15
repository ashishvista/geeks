import random


def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):

        pos = randomPartition(arr, l, r)

        if (pos - l == k - 1):
            return arr[pos]
        if (pos - l > k - 1):  # If position is more,
            return kthSmallest(arr, l, pos - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r,
                           k - pos + l - 1)

    return 999999999999


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i


def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = int(random.random() % n)
    swap(arr, l + pivot, r)
    return partition(arr, l, r)



if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        res = kthSmallest(arr, 0, n - 1, k)
        print(res)