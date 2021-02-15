def sort123(arr, n):
    lo = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 1:
            mid += 1
        elif arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    for i in arr:
        print(i, end=' ')
    print()


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        sort123(arr, n)
