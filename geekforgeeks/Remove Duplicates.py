def removedup(s):
    h = {}
    for c in s:
        if c not in h:
            print(c, end="")
            h[c] = 1


def removedup2(s):
    arr = [False for i in range(256)]
    for c in s:
        arr[ord(c)] = True

    for c in s:
        if arr[ord(c)]:
            print(c, end="")
            arr[ord(c)] = False


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        s = input()
        removedup2(s)
        print()
