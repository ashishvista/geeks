def find_in_stream(arr, n):
    q = []
    hmap = {}

    for c in arr:
        if c in hmap:
            hmap[c] += 1
        else:
            hmap[c] = 1
            q.append(c)
        print_last_nrc(arr, hmap, q)


def print_last_nrc(arr, hmap, q):
    last = None
    while q:
        item = q[0]
        if hmap[item] == 1:
            last = item
            break
        else:
            q.pop(0)

    if last:
        print(last, end=' ')
    else:
        print(-1, end=' ')


if __name__ == '__main__':
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        arr = input().strip().split()
        find_in_stream(arr, n)
        print()
