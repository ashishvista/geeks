def msp(n, arr):
    h = {0: 1}
    d = [0]
    dl = 1
    sum = 0
    for i in range(n):
        sum += arr[i]

    total = sum
    sum = sum // 2
    max = float("-inf")
    for i in range(n):
        c = 0
        for j in range(dl):
            tmp = d[j] + arr[i]
            if tmp not in h:
                h[tmp] = 1
                d.append(tmp)
                c += 1
                if tmp <= sum and max < tmp:
                    max = tmp

        dl += c
    dif = (total - max) - max
    print(dif)


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        msp(n, arr)
