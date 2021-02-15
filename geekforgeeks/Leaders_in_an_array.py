def leaders(arr, n):
    j = n - 2
    max = arr[n - 1]
    res = [max]
    while j >= 0:
        if arr[j] >= max:
            res.append(arr[j])
            max = arr[j]
        j -= 1

    j = len(res) - 1
    while j >= 0:
        print(res[j], end=" ")
        j -= 1


if __name__ == '__main__':
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        leaders(arr, n)
        print()
