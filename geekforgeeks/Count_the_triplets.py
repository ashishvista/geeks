def count(n, arr):
    h = {}
    c = 0
    for i in range(n):
        h[arr[i]] = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if sum in h:
                c += 1
    if c == 0:
        print(-1)
    else:
        print(c)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        count(n, arr)
