import collections

# import sys
# def my_except_hook(exctype, value, traceback):
#     print(exctype,value,traceback)
#
# sys.excepthook = my_except_hook

def getMax(arr, n, k):
    q = collections.deque([])

    for i in range(k):

        while q and int(arr[i]) > int(arr[q[-1]]):
            q.pop()
        q.append(i)

    print(arr[q[0]], end=" ")

    for i in range(k , n):

        while q and q[0] <= i - k:
            q.popleft()

        while q and int(arr[i]) > int(arr[q[-1]]):
            q.pop()

        q.append(i)

        print(arr[q[0]], end=" ")


if __name__ == "__main__":
    tcases = int(input())
    for t in range(tcases):
        n, k = list(map(int, input().strip().split()))
        arr = list(input().strip().split())

        # arr = list(map(int, input().strip().split()))
        getMax(arr, n, k)
        print()
