from collections import deque


def remove(s):
    arr = deque(s)
    n = len(s)
    ld = None  # last deleted character
    i = n - 1
    bool = False
    while i >= 0:
        tmp = arr[i]
        if i != 0 and arr[i] == arr[i - 1]:
            bool = True
            ld = arr[i]
            del arr[i]
            i = i - 1
            del arr[i]
            i = i - 1

        elif arr[i] == ld:
            ld = None
            del arr[i]
            i -= 1
        else:
            ld = None
            i -= 1
    if bool:
        tmp = "".join(arr)
        remove(tmp)
    else:
        for i in arr:
            print(i, end="")


def remove2(s):
    last_removed = [None]
    rem_str = removeUtil2(s, last_removed)
    print(rem_str, end="")


def removeUtil2(s, last_removed):
    n = len(s)
    if n == 1 or n == 0:
        return s
    if s[0] == s[1]:
        # last_removed[0] = s[0]
        while len(s) > 1 and s[0] == s[1]:
            s = s[1:]
        s = s[1:]
        return removeUtil2(s, last_removed)
    else:
        rem_str = removeUtil2(s[1:], last_removed)

        if rem_str and rem_str[0] == s[0]:
            last_removed[0] = rem_str[0]
            return rem_str[1:]
        elif s[0] == last_removed[0]:
            return rem_str
        else:
            last_removed[0] = None
            return s[0] + rem_str


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        s = input()
        remove2(s)
        print()
