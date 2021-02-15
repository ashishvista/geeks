def keyPair(arr, x):
    h = {}
    count = 0
    for i in range(n):
        r = x - arr[i]
        if r in h:
            count += h[r]
        if arr[i] not in h:
            h[arr[i]] = 1
        else:
            h[arr[i]] += 1
    return count


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = keyPair(arr, x)
        print(res)
