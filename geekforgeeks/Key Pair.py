def keyPair(arr, x):
    h = {}
    for i in range(n):
        if arr[i] in h:
            return "Yes"
        else:
            h[x-arr[i]]=1
    return "No"


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res=keyPair(arr, x)
        print(res)
