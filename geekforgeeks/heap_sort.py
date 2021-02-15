def heapify(arr, n, i):
    l_index = 2 * i + 1
    r_index = 2 * i + 2

    largest = i

    if l_index <= n - 1 and arr[l_index] > arr[largest]:
        largest = l_index
    if r_index <= n - 1 and arr[largest] < arr[r_index]:
        largest = r_index

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def buildHeap(arr, n):
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        buildHeap(arr, n)
        print(*arr)
