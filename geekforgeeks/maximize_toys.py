def maximize_toys(n, k, arr):
    arr.sort()
    sum = 0
    c = 0
    for i in arr:
        sum = sum + i
        c = c + 1
        if sum > k:
            s = sum - i
            c = c - 1
            break
    print(c)
    return c


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        maximize_toys(n, k, arr)
