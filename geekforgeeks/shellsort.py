def shellsort(arr):
    n = len(arr)
    interval = n // 2
    while interval >= 1:
        for i in range(interval, n):
            j = i
            while j - interval >= 0 and arr[j] < arr[j - interval]:
                arr[j], arr[j - interval] = arr[j - interval], arr[j]
                j = j - interval
        interval //= 2
    print(arr)

if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        arr = list(map(int, input().strip().split()))
        shellsort(arr)
