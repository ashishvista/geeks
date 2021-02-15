import random


#############################################################################################
def quickSort(k, arr, start, end):
    # if start == end == k:
    #     return arr[start]
    pos = partition(arr, start, end)
    if k == pos:
        return arr[pos]
    elif k < pos:
        res = quickSort(k, arr, start, pos - 1)
    else:
        res = quickSort(k, arr, pos + 1, end)
    return res


def partition(arr, start, end):
    randomizePivot(arr, start, end)
    i = j = 0
    pivot = end
    while i < pivot:
        if arr[i] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j


def randomizePivot(arr, start, end):
    diff = end - start
    v = random.randint(0, diff)
    pivot = start + v
    arr[end], arr[pivot] = arr[pivot], arr[end]


#################################################################################################

def minHeapSort(k, arr, n):
    t = n // 2
    for i in range(t - 1, -1, -1):
        minHeapify(arr, n, i)

    for i in range(1, k + 1):
        kth = arr[0]
        arr[0], arr[n - i] = arr[n - i], arr[0]
        minHeapify(arr, n - i, 0)
    return kth


def minHeapify(arr, n, i):
    # if n == 0 or n == 1:
    #     return
    l = i * 2 + 1
    r = i * 2 + 2

    smallest = i

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, n, smallest)


#########################################################################################

def maxHeapSort(k, arr, n):
    t = k // 2
    for i in range(t - 1, -1, -1):
        maxHeapify(arr, k, i)

    for i in range(k, n):
        if arr[i] < arr[0]:
            arr[0], arr[i] = arr[i], arr[0]
            maxHeapify(arr, k, 0)

    return arr[0]


def maxHeapify(arr, n, i):
    # if n == 0 or n == 1:
    #     return
    l = i * 2 + 1
    r = i * 2 + 2

    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        # res = quickSort(k - 1, arr, 0, n - 1)
        # res = minHeapSort(k, arr, n)
        res = maxHeapSort(k, arr, n)
        print(res)
