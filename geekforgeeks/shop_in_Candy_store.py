def candy(arr, n, k):
    arr.sort()

    l = len(arr) - 1
    min = 0
    i = 0
    while i <= l:
        min += arr[i]
        i += 1
        l -= k
    print(min,end=' ')

    l = len(arr) - 1
    max = 0
    i = 0
    while l>=i:
        max += arr[l]
        l -= 1
        i += k
    print(max)

if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        candy(arr, n, k)
