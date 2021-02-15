# shell sort custom for one element


def customSort(arr1, arr2, m, n):
    total_num = m + n
    interval = total_num // 2
    while interval >= 1:
        for k in range(interval, total_num):
            tmp1 = p(k, m, n, arr1, arr2)
            tmp2 = p(k - interval, m, n, arr1, arr2)
            tarr1 = tmp1[0]
            t1 = tmp1[1]

            tarr2 = tmp2[0]
            t2 = tmp2[1]

            while tarr1[t1] < tarr2[t2]:
                tarr1[t1], tarr2[t2] = tarr2[t2], tarr1[t1]
                k -= interval
                if k - interval < 0:
                    break
                tmp1 = p(k, m, n, arr1, arr2)
                tmp2 = p(k - interval, m, n, arr1, arr2)
                tarr1 = tmp1[0]
                t1 = tmp1[1]
                tarr2 = tmp2[0]
                t2 = tmp2[1]
        interval //= 2


def p(x, m, n, arr1, arr2):
    i = j = None
    if x >= m:
        j = x - m
        return [arr2, j]
    else:
        i = x
        return [arr1, i]


# Merging two sorted arrays with O(1)
# extra space

def minheap(arr, n):
    k = (n // 2) - 1
    for i in range(k, -1, -1):
        heapify(arr, i, n)


def heapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2

    smallest = i

    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest, n)


def maxheap(arr, n):
    k = (n // 2) - 1
    for i in range(k, -1, -1):
        maxHeapify(arr, n, i)


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


def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    minheap(arr2, n)
    i = 0
    while i < m:
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            heapify(arr2, 0, n)
        i += 1
    # arr2.sort()
    maxheap(arr2, n)
    for i in range(n - 1, 0, -1):  #### n-1 size to  2
        arr2[i], arr2[0] = arr2[0], arr2[i]
        maxHeapify(arr2, i, 0)


if __name__ == "__main__":
    # arr1 = [1, 5, 10, 15, 22, 30, 33, 39]
    # arr2 = [0, 1, 2, 11, 18, 30, 40, 50]
    # arr1 = []
    # arr2 = []
    # m, n = 10, 5
    # pp = 50
    # for i in range(m):
    #     arr1.append(randrange(pp))
    #
    # for i in range(n):
    #     arr2.append(randrange(pp))

    # merge(arr1, arr2)
    #
    # for i in range(len(arr1)):
    #     print(arr1[i], end=" ")
    # for j in range(len(arr2)):
    #     print(arr2[j], end=" ")
    # print()
    #
    # customSort(arr1, arr2, m, n)
    # for i in range(m):
    #     print(arr1[i], end=" ")
    # for j in range(n):
    #     print(arr2[j], end=" ")
    # print()

    tcases = int(input())
    for t in range(tcases):
        m, n = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        # if t == 3:
        #     print("hello")
        #     break
        # customSort(arr1, arr2, m, n)
        merge(arr1, arr2)

        for i in range(m):
            print(arr1[i], end=" ")
        for j in range(n):
            print(arr2[j], end=" ")
        print()
