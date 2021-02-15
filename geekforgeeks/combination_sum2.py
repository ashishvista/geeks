def combination(n, arr, sum):
    arr.sort()
    i = s = 0
    h = {}
    comb_util(n, arr, sum, i, s, [], h)
    if h:
        print()
    else:
        print("Empty")


def comb_util(n, arr, sum, i, s, elems, h):
    if s == sum:
        tmp = " "
        tmp = "(" + tmp.join(elems) + ")"
        if tmp in h:
            return 0
        else:
            h[tmp] = 1
            print(tmp, end="")
        return 1
    if s > sum:
        return 0
    if i >= n:
        return 0
    elems_1 = elems.copy()
    elems_2 = elems.copy()
    elems_1.append(str(arr[i]))

    res = comb_util(n, arr, sum, i + 1, s + arr[i], elems_1, h) + comb_util(n, arr, sum, i + 1, s, elems_2, h)

    return res


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        sum = int(input())
        combination(n, arr, sum)
