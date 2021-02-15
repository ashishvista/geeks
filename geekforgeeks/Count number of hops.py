from collections import deque


def count(n):
    arr = deque([1, 2, 4])
    if n <= 3:
        return arr[n - 1]
    t = n - 3
    for i in range(t):
        tmp = arr[0] + arr[1] + arr[2]
        arr.popleft()
        arr.append(tmp)

    return arr[2]


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n = int(input())
        res = count(n)
        print(res)
