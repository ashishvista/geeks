def lis(n, arr):
    lis_arr = [0 for i in range(n)]
    lis_arr[0] = 1
    big_mx = 0
    for i in range(1, n):
        mx = 0
        for j in range(0, i):
            if arr[i] > arr[j]:
                mx = max(mx, lis_arr[j])
        lis_arr[i] = mx + 1
        big_mx = max(big_mx, lis_arr[i])

    print(big_mx)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis(n, arr)
