def smallest(n, k, arr):
    s = 0
    for j in range(n):
        s = s + arr[j]
        if s > k:
            break
    if s <= k:
        return 0

    i = 0
    if j == n - 1:
        return n

    # ssl = j - i + 1  # smallest_subarray_length

    i = 0

    while j <= (n - 1):
        if s > k:
            ssl = j - i + 1
            if ssl == 1:
                return 1
            s -= arr[i]
            i += 1
            continue
        if j == n - 1:
            break
        s -= arr[i]
        s += arr[j + 1]
        i += 1
        j += 1

    return ssl


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = smallest(n, k, arr)
        print(res)
