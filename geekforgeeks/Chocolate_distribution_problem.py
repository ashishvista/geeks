def distribute(arr, n, m):
    arr.sort()
    i = 0
    j = m - 1
    d = arr[j] - arr[i]
    i = i + 1
    j = j + 1
    while j < n:
        temp = arr[j] - arr[i]
        if temp < d:
            d = temp
        j=j+1
        i=i+1
    return d


if __name__ == '__main__':
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        m = int(input())
        print(distribute(arr, n, m))
