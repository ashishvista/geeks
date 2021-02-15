def triplet_sum(arr, n, x):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == x:
                    print(1)
                    return
    print(0)


def triplet_sum2(arr, n, x):
    arr.sort()
    s = x
    for i in range(n - 2):
        s = s - arr[i]
        j = i + 1
        k = n - 1
        while j != k:
            t = arr[j] + arr[k]
            if t > s:
                k -= 1
            elif t < s:
                j += 1
            else:
                print(1)
                return
        s = x
    print(0)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        triplet_sum2(arr, n, x)
