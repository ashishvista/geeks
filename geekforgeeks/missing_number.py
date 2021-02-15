def missing(n, arr):
    osum = n * (n + 1) / 2
    sum = 0
    for i in arr:
        sum += i
    print(int(osum - sum))


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        missing(n, arr)
