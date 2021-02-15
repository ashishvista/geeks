# User function Template for python3
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in arr[], else return 0'''


def findTriplets(arr, n):
    arr.sort()
    s = 0
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
                return 1
        s = 0
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(findTriplets(a, n))
# } Driver Code Ends