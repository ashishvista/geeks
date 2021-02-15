def diagonal(arr, n):
    for i in range(n):
        pd(arr, n, 0, i)

    for i in range(1, n):
        pd(arr, n, i, n - 1)


def pd(arr, n, x, y):
    while x < n and y >= 0:
        print(arr[x][y], end=" ")
        x += 1
        y -= 1


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        tmp = list(map(int, input().strip().split()))
        c = 0
        arr = []
        for i in range(n):
            tt = []
            for j in range(n):
                tt.append(tmp[c])
                c += 1
            arr.append(tt)
        diagonal(arr, n)
        print()
