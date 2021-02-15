def quickSort(arr, low, high):
    if high - low < 1:
        return
    pi = partition2(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)


# def partition(arr, low, high):
#     i = low
#     j = high
#     pivot = high
#
#     while i <= j:
#         if arr[i] > arr[pivot]:
#             arr[i], arr[j] = arr[j], arr[i]
#             if pivot == j:
#                 pivot = i
#             j -= 1
#         else:
#             i += 1
#     arr[j], arr[pivot] = arr[pivot], arr[j]
#     return j


def partition2(arr, low, high):
    pivot = high
    i = low
    j = low

    while j < high:
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        else:
            j += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        quickSort(arr, 0, n - 1)
        for i in arr:
            print(i, end=" ")
        print()
