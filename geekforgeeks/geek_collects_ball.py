def collect(n, m, arr1, arr2):
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    s = 0
    t1 = 0
    t2 = 0
    while i < l1 and j < l2:
        if arr1[i] == arr2[j]:
            t1 += arr1[i]
            t2 += arr2[j]
            p = i
            q = j
            i = i + 1
            j = j + 1

            while i < l1 and arr1[i] == arr1[i - 1]:
                t1 += arr1[i]
                i = i + 1

            while j < l2 and arr2[j] == arr2[j - 1]:
                t2 += arr2[j]
                j = j + 1

            if t1 > t2:
                s += t1
                j = q + 1
            else:
                s += t2
                i = p + 1
            t1 = 0
            t2 = 0


        elif arr1[i] < arr2[j]:
            t1 += arr1[i]
            i = i + 1
        else:
            t2 += arr2[j]
            j = j + 1

    while i < l1:
        t1 += arr1[i]
        i += 1
    while j < l2:
        t2 += arr2[j]
        j += 1

    if t1 > t2:
        s += t1
    else:
        s += t2

    print(s)
    return s


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, m = list(map(int, input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        collect(n, m, arr1, arr2)
