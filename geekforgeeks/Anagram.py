def anagram(a, b):
    if len(a) != len(b):
        print('NO')
        return

    h = {}
    for c in a:
        if c in h:
            h[c] += 1
        else:
            h[c] = 1

    for c in b:
        if c not in h:
            print('NO')
            return
        else:
            h[c] -= 1
            if h[c] == 0:
                del h[c]

    print('YES')


def anagram2(a, b):
    if len(a) != len(b):
        print('NO')
        return

    arr = [0 for i in range(26)]
    for c in a:
        arr[ord(c)-97] += 1

    for c in b:
        arr[ord(c)-97] -= 1

    for i in arr:
        if i != 0:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        a, b = list(input().strip().split(" "))
        anagram2(a, b)

# print(ord('a'))