def minimizeHeights(k, n, arr):
    arr.sort()
    small = arr[0] + k
    big = arr[n - 1] - k
    if big < small:
        t = small
        small = big
        big = t
    diff = arr[n - 1] - arr[0]
    i = 1
    while i <= len(arr) - 2:
        add = arr[i] + k
        sub = arr[i] - k
        if not (add < big or sub > small):
            bdiff = add - big
            sdiff = small - sub
            if bdiff > sdiff:
                small=sub
            else:
                big=add
        i+=1

    print(min(diff, big-small))


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        minimizeHeights(k, n, arr)
