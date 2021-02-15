def merge(arr1, arr2, m, n):
    i = m - 1
    j = n - 1
    while j >= 0:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            customSort(arr1, m)
        j -= 1


# shell sort custom for one element
def customSort(arr, n):
    i = n
    interval = i // 2
    while interval >= 1:
        tmp = i - interval
        tmp2 = arr[tmp]
        while (i - interval) >= 0 and arr[i] < arr[i - interval]:
            arr[i], arr[i - interval] = arr[i - interval], arr[i]
            i -= interval
        interval //= 2


if __name__ == "__main__":
    arr1 = []
    arr2 = []
    m, n = 100, 20
    for i in range(m):
        arr1.append(i)

    for i in range(n):
        arr2.append(2 * i)

    merge(arr1, arr2, m, n)
    for i in range(m):
        print(arr1[i], end=" ")
    for j in range(n):
        print(arr2[j], end=" ")
        # tcases = int(input())
        # for t in range(tcases):
        #     m, n = list(map(int, input().strip().split()))
        #     arr1 = list(map(int, input().strip().split()))
        #     arr2 = list(map(int, input().strip().split()))
        #     if t == 0:
        #         print("hello")
        #         break
        #     merge(arr1, arr2, m, n)
        #     for i in range(m):
        #         print(arr1[i], end=" ")
        #     for j in range(n):
        #         print(arr2[j], end=" ")

        print()
