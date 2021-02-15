def kadane(n, arr):
    max = float("-inf")
    prev = float("-inf")
    for i in range(n):
        if prev < 0:
            c = arr[i]
        else:
            c = prev + arr[i]
        if c > max:
            max = c
        prev = c
    print(max)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        kadane(n, arr)
