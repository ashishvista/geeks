def getEqpoint(n, arr):
    if n == 2:
        return -1
    elif n == 1:
        return 1
    else:
        i = 0
        b = arr[0]

        j = n-1
        e = arr[n-1]

        while i + 1 < j:
            if b < e:
                i += 1
                b += arr[i]
            elif b > e:
                j -= 1
                e += arr[j]
            elif b == e and i + 2 == j:
                return i + 1 + 1
            elif b == e:
                i += 1
                b += arr[i]
        return -1


if __name__ == '__main__':
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(getEqpoint(n, arr))
