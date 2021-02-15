def count(n, arr):
    if n==1:
        return 0
    pp = arr[0]
    p = arr[1]

    for i in range(2, n):
        c = arr[i] + min(p, pp)
        pp, p = p, c
    return min(pp, p)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = count(n, arr)
        print(res)
